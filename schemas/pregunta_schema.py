from utils.ma import ma
from models.pregunta import Pregunta

class PreguntaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Pregunta
        fields = ('id_pregunta', 'descripcion')

pregunta_schema = PreguntaSchema()