from utils.ma import ma
from models.test import Test

class TestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Test
        fields = ('id_test', 'descripcion')

test_schema = TestSchema()