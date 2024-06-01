from utils.ma import ma
from models.especialista import Especialista

class EspecialistaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Especialista
        fields = ('id_especialista', 'descripcion')

especialista_schema = EspecialistaSchema()