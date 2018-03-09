import sqlalchemy as sa
from .project import sa_project

metadata = sa.MetaData()

SlideModel = sa.Table('content_slide', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('model', sa.Text()),
    sa.Column('number', sa.Integer),
    sa.Column('project_id', sa.Integer, sa.ForeignKey(sa_project.c.id), nullable=False),
)
