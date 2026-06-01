from starlette.middleware.base import (
    BaseHTTPMiddleware
)
from fastapi import Request
from fastapi.responses import JSONResponse
from jose import jwt, JWTError

SECRET_KEY = "SUPER_SECRET_KEY"
ALGORITHM = "HS256"


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request: Request,
        call_next
    ):

        public_routes = [
            "/",
            "/docs",
            "/openapi.json",
            "/auth/login",
            "/auth/register"
        ]

        path = request.url.path


        if path in public_routes:

            return await call_next(request)
    

        auth_header = request.headers.get(
            "Authorization"
        )

        if not auth_header:

            return JSONResponse(
                status_code=401,
                content={
                    "success": False,
                    "message":
                        "Authorization token missing"
                }
            )

        try:

            token = auth_header.split(" ")[1]

        except Exception:

            return JSONResponse(
                status_code=401,
                content={
                    "success": False,
                    "message":
                        "Invalid authorization format"
                }
            )


        try:

            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=[ALGORITHM]
            )

            request.state.user = payload

        except JWTError:

            return JSONResponse(
                status_code=401,
                content={
                    "success": False,
                    "message":
                        "Invalid or expired token"
                }
            )