from utils.db import db

class PacienteTest(db.Model):
    __tablename__ = "paciente_test"

    test_id = db.Column(db.Integer, db.ForeignKey('test.id_test'), primary_key=True)
    pac_id = db.Column(db.Integer, db.ForeignKey('paciente.pac_id'), primary_key=True)
    pt_fecha_realizacion = db.Column(db.DateTime, nullable=False)
    pt_resultado = db.Column(db.Integer, nullable=False)

    test = db.relationship('Test', backref=db.backref('paciente_tests', lazy=True))
    paciente = db.relationship('Paciente', backref=db.backref('paciente_tests', lazy=True))

    def __init__(self, pt_fecha_realizacion, pt_resultado, test_id, pac_id):
        self.test_id = test_id
        self.pac_id = pac_id
        self.pt_fecha_realizacion = pt_fecha_realizacion
        self.pt_resultado = pt_resultado
