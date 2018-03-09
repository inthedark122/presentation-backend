from schematics.models import Model
from schematics.types import IntType, StringType


class ProjectDetailSerializer(Model):
    id = IntType()
    title = StringType()
    name = StringType()
