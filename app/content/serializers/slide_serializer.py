from schematics.models import Model
from schematics.types import IntType, StringType, IntType


class SlideDetailSerializer(Model):
    id = IntType()
    model = StringType()
    number = IntType()
    project_id = IntType()
