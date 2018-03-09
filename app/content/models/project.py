# import sqlalchemy as sa

# metadata = sa.MetaData()

from sqlalchemy import Column, DateTime, Integer, Sequence, String, Text, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProjectModel(Base):
    __tablename__ = 'content_project'
    id = Column(Integer, Sequence('msg_id_seq'), primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    title = Column(String(255))


sa_project = ProjectModel.__table__

# ProjectModel = sa.Table("content_project", metadata, 
#     sa.Column('id', sa.Integer, primary_key=True),
#     sa.Column('name', sa.String(255)),
#     sa.Column('title', sa.String(255)),
# )
