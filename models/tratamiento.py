from utils.db import db

class Tratamiento(db.Model):
    __tablename__ = "tratamiento"

    id_tratamiento = db.Column(db.SmallInteger, primary_key=True)
    descripcion = db.Column(db.String(255))

    def __init__(self, descripcion):
        self.descripcion = descripcion