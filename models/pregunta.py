from utils.db import db

class Pregunta(db.Model):
    __tablename__ = "pregunta"

    id_pregunta = db.Column(db.SmallInteger, primary_key=True)
    id_test = db.Column(db.SmallInteger, db.ForeignKey('test.id_test'))
    descripcion = db.Column(db.String(55))

    test = db.relationship('Test', backref=db.backref('preguntas', lazy=True))

    def __init__(self, descripcion, id_test):
        self.descripcion = descripcion
        self.id_test = id_test