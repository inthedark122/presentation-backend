import base64
from pathlib import Path

from aiohttp import web
from aiopg.sa import create_engine
from sqlalchemy.engine.url import URL

import aiohttp_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from .settings import Settings
from .routes import setup_routes


THIS_DIR = Path(__file__).parent
BASE_DIR = THIS_DIR.parent


def pg_dsn(settings: Settings) -> str:
    """
    :param settings: settings including connection settings
    :return: DSN url suitable for sqlalchemy and aiopg.
    """
    return str(URL(
        database=settings.DB_NAME,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        username=settings.DB_USER,
        drivername='postgres',
    ))


async def startup(app: web.Application):
    app['db'] = await create_engine(pg_dsn(app['settings']), loop=app.loop)


async def cleanup(app: web.Application):
    app['db'].close()
    await app['db'].wait_closed()


def create_app():
    app = web.Application()
    settings = Settings()
    app.update(
        name='presentation-backend',
        settings=settings
    )

    app.on_startup.append(startup)
    app.on_cleanup.append(cleanup)

    secret_key = base64.urlsafe_b64decode(settings.COOKIE_SECRET)
    aiohttp_session.setup(app, EncryptedCookieStorage(secret_key))

    setup_routes(app)
    return app
