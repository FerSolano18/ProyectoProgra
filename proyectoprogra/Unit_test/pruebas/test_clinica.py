import unittest
import pandas as pd
from Clases.clase_clinica import Clinica

class TestClinica(unittest.TestCase):
    def test_init(self):
        clinica = Clinica()
        self.assertEqual(clinica.informacion_csv, 'informacion.csv')
        self.assertEqual(clinica.pacientes_csv, 'pacientes.csv')
        self.assertIsInstance(clinica.terapeutas_disponibles, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()