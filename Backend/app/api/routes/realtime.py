import asyncio
from datetime import datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(
    prefix="/realtime",
    tags=["Real-Time Forecasting"]
)


class ConnectionManager:

    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):

        await websocket.accept()

        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):

        self.active_connections.remove(websocket)

    async def send_live_data(self, data: dict):

        for connection in self.active_connections:

            await connection.send_json(data)


manager = ConnectionManager()


@router.websocket("/dashboard")
async def realtime_dashboard(websocket: WebSocket):

    await manager.connect(websocket)

    try:

        while True:

            realtime_data = {

                "live_sales": 25000,

                "forecast_demand": 27800,

                "inventory_status": "Stable",

                "active_users": 142,

                "system_status": "Running",

                "timestamp": str(datetime.utcnow())
            }

            await manager.send_live_data(
                realtime_data
            )

            await asyncio.sleep(3)

    except WebSocketDisconnect:

        manager.disconnect(websocket)


@router.get("/status")
def realtime_status():

    return {

        "realtime_engine": "Active",

        "connected_clients":
            len(manager.active_connections),

        "refresh_interval": "3 seconds",

        "status": "Running"
    }


@router.get("/live-sales")
def live_sales_monitoring():

    return {

        "today_sales": 450000,

        "hourly_sales": 22000,

        "top_product": "Laptop",

        "sales_growth": "12%"
    }


@router.get("/forecast-refresh")
def forecast_refresh():

    return {

        "forecast_status": "Updated",

        "next_refresh": "3 seconds",

        "ai_engine": "Active"
    }