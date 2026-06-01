import time
import logging

from fastapi import Request
from starlette.middleware.base import (
    BaseHTTPMiddleware
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("api_logger")


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request: Request,
        call_next
    ):

        start_time = time.time()

        method = request.method
        path = request.url.path
        client = request.client.host

        logger.info(
            f"Request Started | "
            f"Method: {method} | "
            f"Path: {path} | "
            f"Client: {client}"
        )

        response = await call_next(request)

        process_time = round(
            time.time() - start_time,
            4
        )

        logger.info(
            f"Request Completed | "
            f"Status: {response.status_code} | "
            f"Time: {process_time}s"
        )

        response.headers[
            "X-Process-Time"
        ] = str(process_time)

        return response