from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import shutil
import os
import pandas as pd

from app.core.database import get_db
from app.models.dataset import Dataset
from app.utils.auth import get_current_user

router = APIRouter(
    prefix="/datasets",
    tags=["Datasets"]
)

UPLOAD_DIR = "storage/datasets"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_dataset(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    # File validation
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(
            status_code=400,
            detail="Only CSV and XLSX files allowed"
        )

    # Save file
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Read dataset
    try:
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid dataset file"
        )

    # Store in database
    dataset = Dataset(
        filename=file.filename,
        rows=df.shape[0],
        columns=df.shape[1],
        uploaded_by=current_user.id
    )

    db.add(dataset)
    db.commit()
    db.refresh(dataset)

    return {
        "message": "Dataset uploaded successfully",
        "dataset_id": dataset.id,
        "rows": dataset.rows,
        "columns": dataset.columns
    }


@router.get("/")
def get_datasets(
    db: Session = Depends(get_db)
):

    datasets = db.query(Dataset).all()

    return datasets


@router.delete("/{dataset_id}")
def delete_dataset(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    dataset = db.query(Dataset).filter(
        Dataset.id == dataset_id
    ).first()

    if not dataset:
        raise HTTPException(
            status_code=404,
            detail="Dataset not found"
        )

    db.delete(dataset)
    db.commit()

    return {
        "message": "Dataset deleted successfully"
    }