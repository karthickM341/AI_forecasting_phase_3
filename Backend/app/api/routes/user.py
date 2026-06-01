from datetime import datetime
from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

users_db = []


@router.post("/create")
def create_user(data: dict):

    user = {
        "id": len(users_db) + 1,
        "username": data["username"],
        "email": data["email"],
        "role": data["role"],
        "created_at": datetime.utcnow()
    }

    users_db.append(user)

    return {
        "message": "User created successfully",
        "user": user
    }


@router.get("/")
def get_users():

    return {
        "total_users": len(users_db),
        "users": users_db
    }


@router.get("/{user_id}")
def get_single_user(user_id: int):

    for user in users_db:

        if user["id"] == user_id:

            return user

    return {
        "message": "User not found"
    }


@router.put("/update/{user_id}")
def update_user(user_id: int, data: dict):

    for user in users_db:

        if user["id"] == user_id:

            user["username"] = data["username"]
            user["email"] = data["email"]
            user["role"] = data["role"]

            return {
                "message": "User updated successfully",
                "user": user
            }

    return {
        "message": "User not found"
    }


@router.delete("/delete/{user_id}")
def delete_user(user_id: int):

    for user in users_db:

        if user["id"] == user_id:

            users_db.remove(user)

            return {
                "message": "User deleted successfully"
            }

    return {
        "message": "User not found"
    }


@router.get("/roles/all")
def user_roles():

    return {
        "roles": [
            "Super Admin",
            "Analyst",
            "Viewer"
        ]
    }


@router.get("/activity/logs")
def user_activity_logs():

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