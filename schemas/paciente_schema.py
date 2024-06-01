from utils.ma import ma
from models.paciente import Paciente

class PacienteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Paciente
        fields = ('id_paciente', 'descripcion')

paciente_schema = PacienteSchema()