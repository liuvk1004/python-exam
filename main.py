from fastapi import FastAPI, WebSocket

app = FastAPI()


class ConnectionManager:

    def __init__(self, active_connections={}):
        self.active_connections = active_connections
        pass

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections[username] = websocket
        await websocket.send_text("Login Successfully!")
        pass

    def disconnect(self, websocket: WebSocket):
        websocket.close()
        self.active_connections.pop(websocket)
        pass

    async def broadcast(self, message: str, username: str):
        for connection in self.active_connections:
            if connection != username:
                await self.active_connections[connection].send_text("User %s says: %s " % (username, message))
            pass


manager = ConnectionManager()


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)

    while True:
        message = await websocket.receive_text()
        if message == "exit":
            await websocket.send_text("Logout successfully!")
            await websocket.close()
            break
        await manager.broadcast(message, username)
    pass


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
