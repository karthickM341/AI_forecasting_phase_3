from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.database import get_db
from app.models.user import User
from app.models.forecast import Forecast
from app.models.dataset import Dataset
from app.utils.auth import get_current_user


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)



def admin_only(current_user: User = Depends(get_current_user)):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user



@router.get("/dashboard")
def admin_dashboard(
    db: Session = Depends(get_db),
    admin: User = Depends(admin_only)
):

    total_users = db.query(User).count()

    total_forecasts = db.query(Forecast).count()

    total_datasets = db.query(Dataset).count()

    return {
        "total_users": total_users,
        "total_forecasts": total_forecasts,
        "total_datasets": total_datasets
    }



@router.get("/users")
def get_users(
    db: Session = Depends(get_db),
    admin: User = Depends(admin_only)
):

    users = db.query(User).all()

    return users


@router.delete("/user/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    admin: User = Depends(admin_only)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }


@router.get("/forecast-report")
def forecast_report(
    db: Session = Depends(get_db),
    admin: User = Depends(admin_only)
):

    avg_accuracy = db.query(
        func.avg(Forecast.accuracy)
    ).scalar()

    return {
        "average_accuracy": round(avg_accuracy or 0, 2)
    }