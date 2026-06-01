from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

SECRET_KEY = "SUPER_SECRET_KEY"
ALGORITHM = "HS256"

security = HTTPBearer()

def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload

    except JWTError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

def role_required(allowed_roles: list):

    def checker(user=Depends(verify_token)):

        user_role = user.get("role")

        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied"
            )
        return user
    return checker


def super_admin_only():

    return role_required(["Super Admin"])

def analyst_only():

    return role_required([
        "Super Admin",
        "Analyst"
    ])

def viewer_access():

    return role_required([
        "Super Admin",
        "Analyst",
        "Viewer"
    ])