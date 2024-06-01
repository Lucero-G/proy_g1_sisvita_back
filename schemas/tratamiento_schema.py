from utils.ma import ma
from models.tratamiento import Tratamiento

class TratamientoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tratamiento
        fields = ('id_tratamiento', 'descripcion')

tratamiento_schema = TratamientoSchema()