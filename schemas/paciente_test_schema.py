from utils.ma import ma
from models.paciente_test import PacienteTest

class PacienteTestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PacienteTest
        fields = ('id_paciente_test', 'descripcion')

paciente_test_schema = PacienteTestSchema()