from aiohttp import web
from sqlalchemy.sql.expression import select, delete, insert
from ..models import sa_slide
from ..serializers import SlideDetailSerializer

slide_routes = web.RouteTableDef()


@slide_routes.get('/projects/{project_id}/slides')
async def list_get_view(request):
    async with request.app['db'].acquire() as conn:
        project_id = request.match_info['project_id']
        query = sa_slide.select().where(sa_slide.c.project_id==project_id).order_by(sa_slide.c.id.asc())
        result = await conn.execute(query)
        slides = await result.fetchall()

        return web.json_response([
            SlideDetailSerializer(slide).to_primitive()
            for slide
            in slides
        ])


@slide_routes.post('/projects/{project_id}/slides')
async def add_view(request):
    async with request.app['db'].acquire() as conn:
        project_id = request.match_info['project_id']
        data = await request.json()

        slide_id = await conn.scalar(
            sa_slide.insert().values(
                model=data["model"],
                number=data["number"],
                project_id=project_id,
            )
        )

        result = await conn.execute(
            sa_slide.select().where(sa_slide.c.id == slide_id)
        )

        slide = await result.fetchone()

        return web.json_response(SlideDetailSerializer(slide).to_primitive())


@slide_routes.post('/slides/{slide_id}')
async def update_view(request):
    async with request.app['db'].acquire() as conn:
        slide_id = request.match_info['slide_id']
        data = await request.json()

        await conn.execute(
            sa_slide.update().\
                where(sa_slide.c.id == slide_id).\
                values(
                    number=data["number"],
                    model=data["model"],
                )
        )

        result = await conn.execute(
            sa_slide.select().where(sa_slide.c.id == slide_id)
        )

        slide = await result.fetchone()

        return web.json_response(SlideDetailSerializer(slide).to_primitive())

@slide_routes.delete('/slides/{slide_id}')
async def delete_view(request):
    async with request.app['db'].acquire() as conn:
        await conn.execute(sa_slide.delete().where(sa_slide.c.id == request.match_info['slide_id']))

        return web.json_response({"success": True})
