from utils.db import db

class Especialista(db.Model):
    __tablename__ = "especialista"

    id_especialista = db.Column(db.SmallInteger, primary_key=True)

    def __init__(self):
        pass