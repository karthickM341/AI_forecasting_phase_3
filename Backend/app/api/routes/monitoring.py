import psutil
from datetime import datetime

from fastapi import APIRouter

router = APIRouter(
    prefix="/monitoring",
    tags=["Monitoring"]
)


@router.get("/system")
def system_monitoring():

    return {
        "cpu_usage": f"{psutil.cpu_percent()}%",
        "memory_usage": f"{psutil.virtual_memory().percent}%",
        "disk_usage": f"{psutil.disk_usage('/').percent}%",
        "timestamp": datetime.utcnow()
    }


@router.get("/health")
def health_check():

    return {
        "status": "healthy",
        "server": "running",
        "timestamp": datetime.utcnow()
    }


@router.get("/performance")
def performance_metrics():

    return {
        "active_users": 125,
        "api_requests": 5400,
        "forecast_requests": 890,
        "response_time": "120ms"
    }


@router.get("/forecast-history")
def forecast_history():

    history = [
        {
            "product": "Laptop",
            "forecast": 1200,
            "date": "2026-05-20"
        },
        {
            "product": "Mobile",
            "forecast": 2400,
            "date": "2026-05-21"
        }
    ]

    return {
        "history": history
    }


@router.get("/logs")
def activity_logs():

    logs = [
        {
            "user": "admin",
            "activity": "Generated Forecast",
            "time": "10:30 AM"
        },
        {
            "user": "analyst",
            "activity": "Uploaded Dataset",
            "time": "11:15 AM"
        }
    ]

    return {
        "logs": logs
    }