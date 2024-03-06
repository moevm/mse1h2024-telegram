from fastapi import FastAPI
from .routers import ping
app = FastAPI()

app.include_router(ping.router)
