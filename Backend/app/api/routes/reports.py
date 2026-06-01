from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.database import get_db
from app.models.forecast import Forecast
from app.models.dataset import Dataset
from app.models.user import User

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/system")
def system_report(db: Session = Depends(get_db)):

    total_users = db.query(User).count()
    total_datasets = db.query(Dataset).count()
    total_forecasts = db.query(Forecast).count()

    completed_forecasts = db.query(Forecast).filter(
        Forecast.status == "completed"
    ).count()

    failed_forecasts = db.query(Forecast).filter(
        Forecast.status == "failed"
    ).count()

    return {
        "total_users": total_users,
        "total_datasets": total_datasets,
        "total_forecasts": total_forecasts,
        "completed_forecasts": completed_forecasts,
        "failed_forecasts": failed_forecasts
    }


@router.get("/forecast")
def forecast_report(db: Session = Depends(get_db)):

    forecasts = db.query(Forecast).all()

    report = []

    for forecast in forecasts:
        report.append({
            "forecast_id": forecast.id,
            "model_name": forecast.model_name,
            "accuracy": forecast.accuracy_score,
            "status": forecast.status
        })

    return {
        "forecast_reports": report
    }

@router.get("/top-users")
def top_users_report(db: Session = Depends(get_db)):

    users = db.query(
        Forecast.user_id,
        func.count(Forecast.id).label("forecast_count")
    ).group_by(
        Forecast.user_id
    ).all()

    result = []

    for user_data in users:

        user = db.query(User).filter(
            User.id == user_data.user_id
        ).first()

        result.append({
            "user_id": user.id,
            "username": user.username,
            "forecast_count": user_data.forecast_count
        })

    return {
        "top_users": result
    }