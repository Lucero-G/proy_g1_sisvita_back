from utils.db import db

class Paciente(db.Model):
    __tablename__ = "paciente"

    id_paciente = db.Column(db.SmallInteger, primary_key=True)
    nombre = db.Column(db.String(35))
    apellido = db.Column(db.String(35))
    dni = db.Column(db.String(8))
    direccion = db.Column(db.String(55))
    telefono = db.Column(db.String(9))
    correo = db.Column(db.String(35))
    password = db.Column(db.String(10))

    def __init__(self, nombre, apellido, dni, direccion, telefono, correo, password):
        self.nombre = nombre
        self.apellido= apellido
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.correo = password