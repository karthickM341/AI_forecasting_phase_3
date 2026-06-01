from fastapi import WebSocket
from typing import List
import json


class ConnectionManager:

    def __init__(self):

        self.active_connections: List[WebSocket] = []


    async def connect(self, websocket: WebSocket):

        await websocket.accept()

        self.active_connections.append(websocket)


    def disconnect(self, websocket: WebSocket):

        if websocket in self.active_connections:

            self.active_connections.remove(websocket)


    async def send_personal_message(
        self,
        message: dict,
        websocket: WebSocket
    ):

        await websocket.send_text(
            json.dumps(message)
        )

    async def broadcast(self, message: dict):

        disconnected_clients = []

        for connection in self.active_connections:

            try:

                await connection.send_text(
                    json.dumps(message)
                )

            except Exception:

                disconnected_clients.append(
                    connection
                )

        for client in disconnected_clients:

            self.disconnect(client)


    def total_connections(self):

        return len(self.active_connections)
