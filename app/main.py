from fastapi import FastAPI

from app.api.routers import api_router
from app.events import startup, shutdown

app = FastAPI()
app.add_event_handler(
    "startup",
    startup(),
)
app.add_event_handler(
    "shutdown",
    shutdown(),
)

app.include_router(api_router)
