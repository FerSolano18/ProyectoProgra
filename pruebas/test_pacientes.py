import unittest

# Clase pacientes
class Pacientes:
    def __init__(self, nombre, apellido, cedula, telefono, correo, direccion, terapeuta, razon, notas, fecha, metodo_pago):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.terapeuta = terapeuta
        self.razon = razon
        self.notas = notas
        self.fecha = fecha
        self.metodo_pago = metodo_pago


class TestPacientes(unittest.TestCase):
    def test_init(self):
        paciente = Pacientes("Maria", "Solano", "300000111", "1234-5824", "maria@gmail.com", "Orosi", "Solano", "Fisioterapia", "AAAA", "23/4", "Tarjeta")
        self.assertEqual(paciente.nombre, "Maria")
        self.assertEqual(paciente.apellido, "Solano")
        self.assertEqual(paciente.cedula, "300000111")
        self.assertEqual(paciente.telefono, "1234-5824")
        self.assertEqual(paciente.correo, "maria@gmail.com")
        self.assertEqual(paciente.direccion, "Orosi")
        self.assertEqual(paciente.terapeuta, "Solano")
        self.assertEqual(paciente.razon, "Fisioterapia")
        self.assertEqual(paciente.notas, "AAAA")
        self.assertEqual(paciente.fecha, "23/4")
        self.assertEqual(paciente.metodo_pago, "Tarjeta")

if __name__ == '__main__':
    unittest.main()
