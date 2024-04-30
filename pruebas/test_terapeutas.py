import unittest
from Clases.clase_terapeutas import TerapeutaDisponible

class TestTerapeutaDisponible(unittest.TestCase):
    def test_terapeuta_attributes(self):
        terapeuta = TerapeutaDisponible("Juan", "Perez", "Lunes", "2022-01-01", "10:00", "Sede A", "Psicología", 0)
        self.assertEqual(terapeuta.nombre, "Juan")
        self.assertEqual(terapeuta.apellido, "Perez")
        self.assertEqual(terapeuta.dia, "Lunes")
        self.assertEqual(terapeuta.fecha, "2022-01-01")
        self.assertEqual(terapeuta.hora, "10:00")
        self.assertEqual(terapeuta.sede, "Sede A")
        self.assertEqual(terapeuta.especialidad, "Psicología")
        self.assertEqual(terapeuta.tarifa, 0)

if __name__ == '__main__':
    unittest.main()
