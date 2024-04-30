import pandas as pd

# Clase pacientes
class Pacientes:
    def __init__(self, nombre, apellidos, cedula, telefono, correo, direccion, terapeuta, razon, notas):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.terapeuta = terapeuta
        self.razon = razon
        self.notas = notas


