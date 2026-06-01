from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.database import get_db
from app.models.user import User
from app.models.dataset import Dataset
from app.models.forecast import Forecast

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/dashboard")
def dashboard_analytics(db: Session = Depends(get_db)):

    total_users = db.query(User).count()

    total_datasets = db.query(Dataset).count()

    total_forecasts = db.query(Forecast).count()

    latest_forecasts = (
        db.query(Forecast)
        .order_by(Forecast.id.desc())
        .limit(5)
        .all()
    )

    recent_data = []

    for forecast in latest_forecasts:
        recent_data.append({
            "forecast_id": forecast.id,
            "forecast_name": forecast.forecast_name,
            "model": forecast.model_name
        })

    return {
        "success": True,
        "analytics": {
            "total_users": total_users,
            "total_datasets": total_datasets,
            "total_forecasts": total_forecasts,
            "recent_forecasts": recent_data
        }
    }


@router.get("/models")
def model_analytics(db: Session = Depends(get_db)):

    models = (
        db.query(
            Forecast.model_name,
            func.count(Forecast.id).label("total")
        )
        .group_by(Forecast.model_name)
        .all()
    )

    data = []

    for model in models:
        data.append({
            "model_name": model[0],
            "total_usage": model[1]
        })

    return {
        "success": True,
        "models": data
    }


@router.get("/users")
def user_analytics(db: Session = Depends(get_db)):

    users = db.query(User).all()

    result = []

    for user in users:

        forecast_count = (
            db.query(Forecast)
            .filter(Forecast.user_id == user.id)
            .count()
        )

        result.append({
            "user_id": user.id,
            "username": user.username,
            "total_forecasts": forecast_count
        })

    return {
        "success": True,
        "users": result
    }