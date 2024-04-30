import unittest
from Clases.clase_terapeutas import TerapeutaDisponible

class TestTerapeutaDisponible(unittest.TestCase):
    def test_init(self):
        terapeuta = TerapeutaDisponible("Lili", "Lunes", "2022-01-01", "10:00", "Cartago")
        self.assertEqual(terapeuta.nombre, "Lili")
        self.assertEqual(terapeuta.dia, "Lunes")
        self.assertEqual(terapeuta.fecha, "2022-01-01")
        self.assertEqual(terapeuta.hora, "10:00")
        self.assertEqual(terapeuta.sede, "Cartago")

if __name__ == '__main__':
    unittest.main()
