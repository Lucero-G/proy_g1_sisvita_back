from utils.ma import ma
from models.cita import Cita

class CitaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Cita
        fields = ('id_cita', 'descripcion')

cita_schema = CitaSchema()