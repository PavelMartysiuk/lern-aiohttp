from aiohttp import web
from app1.urls import add_urls
from aiopg.sa import create_engine


def create_app(config: dict):
    app = web.Application()
    add_urls(app)
    config.pop('sqlalchemy')
    app['config.yaml'] = config
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)
    return app


async def on_start(app):
    app['db'] = await create_engine(**app['config.yaml'])


async def on_shutdown(app):
    app['db'].close()
    await app['db'].wait_closed()
