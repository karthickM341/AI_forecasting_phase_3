from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.auth import (router as auth_router)
from app.api.routes.user import router as user_router
from app.api.routes.inventory import router as inventory_router
from app.api.routes.monitoring import router as monitoring_router
from app.api.routes.optimization import router as optimization_router
from app.api.routes.realtime import router as realtime_router
from fastapi.responses import FileResponse
from app.middleware.auth_middleware import (
    AuthMiddleware
)
from app.middleware.logging_middleware import (
    LoggingMiddleware
)
from app.middleware.monitoring_middleware import (
    MonitoringMiddleware
)
from app.core.scheduler import start_scheduler
from app.core.database import (
    Base,
    engine
)
from app.models.user import User

Base.metadata.create_all(
    bind=engine
)
app = FastAPI(
    title="AI Demand Forecasting API",
    version="3.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(AuthMiddleware)
app.add_middleware(LoggingMiddleware)
app.add_middleware(MonitoringMiddleware)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(inventory_router)
app.include_router(monitoring_router)
app.include_router(optimization_router)
app.include_router(realtime_router)

start_scheduler()

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")

@app.get("/")
def root():

    return {

        "message":
            "AI Demand Forecasting Backend Running",
        "version": "3.0",
        "status": "Active"
    }