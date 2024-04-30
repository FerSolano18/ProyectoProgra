import unittest
from Clases.clase_pacientes import Pacientes

class TestPacientes(unittest.TestCase):
    def test_init(self):
        paciente = Pacientes("Maria", "Solano", "123456", "123456789", "maria@gmail.com", "Orosi", "Lili", "Fisioterapia", "no aplica")
        self.assertEqual(paciente.nombre, "Maria")
        self.assertEqual(paciente.apellidos, "Solano")
        self.assertEqual(paciente.cedula, "123456")
        self.assertEqual(paciente.telefono, "123456789")
        self.assertEqual(paciente.correo, "maria@gmail.com")
        self.assertEqual(paciente.direccion, "Orosi")
        self.assertEqual(paciente.terapeuta, "Lili")
        self.assertEqual(paciente.razon, "Fisioterapia")
        self.assertEqual(paciente.notas, "no aplica")

if __name__ == '__main__':
    unittest.main()