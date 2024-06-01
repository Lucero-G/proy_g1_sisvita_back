from utils.db import db

class Cita(db.Model):
    __tablename__ = "cita"

    id_cita = db.Column(db.SmallInteger, primary_key=True)

    def __init__(self, descripcion):
        pass