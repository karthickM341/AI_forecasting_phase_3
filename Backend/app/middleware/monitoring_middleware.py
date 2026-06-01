import time
import psutil

from fastapi import Request
from starlette.middleware.base import (
    BaseHTTPMiddleware
)

from fastapi.responses import JSONResponse


class MonitoringMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request: Request,
        call_next
    ):

        start_time = time.time()


        cpu_before = psutil.cpu_percent()

        memory_before = (
            psutil.virtual_memory().percent
        )


        response = await call_next(request)


        cpu_after = psutil.cpu_percent()

        memory_after = (
            psutil.virtual_memory().percent
        )

        process_time = round(
            time.time() - start_time,
            4
        )


        response.headers["X-Process-Time"] = (
            str(process_time)
        )

        response.headers["X-CPU-Usage"] = (
            f"{cpu_after}%"
        )

        response.headers["X-Memory-Usage"] = (
            f"{memory_after}%"
        )

        return response