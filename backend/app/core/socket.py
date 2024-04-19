from socketio import AsyncServer, ASGIApp
from app.config.settings import settings

sio = AsyncServer(
    async_mode="asgi",
    cors_allowed_origins="*"
)

sio_app = ASGIApp(
    socketio_server=sio,
    socketio_path=settings.SOCKET_STR
)
