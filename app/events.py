from typing import Callable

from app.db.events import close_db, init_db


def startup() -> Callable:
    """
    Create startup events handler.

    Should be run before the app starts. Here should be init for db, redis, etc.
    """

    async def start_app() -> None:  # noqa: WPS430
        await init_db()

    return start_app


def shutdown() -> Callable:
    """
    Shutdown events handler.

    Should be run when the app is shutting down. Here should close db, redis, etc.
    """

    async def stop_app() -> None:  # noqa: WPS430
        await close_db()

    return stop_app
