from aiohttp import web
from .content import project_routes

async def ping(request):
    return web.Response(text="Ok")

def setup_routes(app):
    app.router.add_get("/ping", ping)
    app.router.add_routes(project_routes)
