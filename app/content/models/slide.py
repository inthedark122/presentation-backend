from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SlideModel(Base):
    __tablename__ = 'content_slide'
    id = Column(Integer, primary_key=True)
    model = Column(Text)
    number = Column(Integer)
    project_id = Column(Integer, ForeignKey('content_project.id'))
    project = relationship("ProjectModel", back_populates="slide")


sa_slide = SlideModel.__table__
