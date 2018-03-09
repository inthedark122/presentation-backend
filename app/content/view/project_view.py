from aiohttp import web
from sqlalchemy.sql.expression import select, delete, insert
from ..models import sa_project
from ..serializers import ProjectDetailSerializer

project_routes = web.RouteTableDef()


@project_routes.get('/projects')
async def list_get_view(request):
    async with request.app['db'].acquire() as conn:
        result = await conn.execute(sa_project.select())
        projects = await result.fetchall()

        return web.json_response([
            ProjectDetailSerializer(project).to_primitive()
            for project
            in projects
        ])


@project_routes.post('/projects')
async def add_view(request):
    async with request.app['db'].acquire() as conn:
        data = await request.json()

        project_id = await conn.scalar(
            sa_project.insert().values(
                name=data["name"],
                title=data["title"],
            )
        )

        result = await conn.execute(
            sa_project.select().where(sa_project.c.id == project_id)
        )

        project = await result.fetchone()

        return web.json_response(ProjectDetailSerializer(project).to_primitive())

@project_routes.delete('/projects/{project_id}')
async def delete_view(request):
    async with request.app['db'].acquire() as conn:
        await conn.execute(sa_project.delete().where(sa_project.c.id == request.match_info['project_id']))

        return web.json_response({success: True})
