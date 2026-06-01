from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.notification import Notification
from app.schemas.notification import NotificationCreate

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


# CREATE NOTIFICATION
@router.post("/")
def create_notification(
    data: NotificationCreate,
    db: Session = Depends(get_db)
):
    notification = Notification(
        title=data.title,
        message=data.message,
        user_id=data.user_id
    )

    db.add(notification)
    db.commit()
    db.refresh(notification)

    return {
        "message": "Notification created",
        "data": notification
    }


# GET ALL NOTIFICATIONS
@router.get("/")
def get_notifications(db: Session = Depends(get_db)):
    notifications = db.query(Notification).all()

    return notifications


# GET SINGLE NOTIFICATION
@router.get("/{notification_id}")
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):
    notification = (
        db.query(Notification)
        .filter(Notification.id == notification_id)
        .first()
    )

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    return notification


# DELETE NOTIFICATION
@router.delete("/{notification_id}")
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):
    notification = (
        db.query(Notification)
        .filter(Notification.id == notification_id)
        .first()
    )

    if not notification:
        raise HTTPException(
            status_code=404,
            detail="Notification not found"
        )

    db.delete(notification)
    db.commit()

    return {
        "message": "Notification deleted"
    }