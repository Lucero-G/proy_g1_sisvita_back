from utils.db import db

class Test(db.Model):
    __tablename__ = "test"

    id_test = db.Column(db.SmallInteger, primary_key=True)
    nombre = db.Column(db.String(30))
    tipo = db.Column(db.String(30))

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo