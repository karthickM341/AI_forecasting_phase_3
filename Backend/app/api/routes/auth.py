from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)
from sqlalchemy.orm import Session
from passlib.context import (CryptContext)
from app.core.database import (get_db)
from app.models.user import User
from app.core.security import (
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

pwd_context = CryptContext(
    schemes=["bcrypt"]
)


# ==========================================
# REGISTER
# ==========================================

@router.post("/register")
def register(
    data: dict,
    db: Session = Depends(get_db)
):

    hashed_password = (
        pwd_context.hash(
            data["password"]
        )
    )

    user = User(

        username=data["username"],

        email=data["email"],

        password=hashed_password,

        role=data["role"]
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return {
        "message":
            "User registered successfully"
    }


# ==========================================
# LOGIN
# ==========================================

@router.post("/login")
def login(
    data: dict,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == data["email"]
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    valid_password = (
        pwd_context.verify(
            data["password"],
            user.password
        )
    )

    if not valid_password:

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token({

        "id": user.id,

        "email": user.email,

        "role": user.role
    })

    return {

        "access_token": token,

        "token_type": "bearer"
    }