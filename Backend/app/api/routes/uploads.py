from fastapi import APIRouter, UploadFile, File
import shutil
import os

router = APIRouter(prefix="/reports",tags=["Reports"])

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/upload")

async def upload_dataset(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Dataset uploaded successfully",
        "filename": file.filename
    }