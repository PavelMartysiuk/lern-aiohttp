from aiohttp import web
from urls import add_urls


async def create_app():
    app = web.Application()
    add_urls(app)
    return app
