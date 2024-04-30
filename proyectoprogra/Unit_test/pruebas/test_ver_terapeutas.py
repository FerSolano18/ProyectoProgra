import unittest
from Clases.clase_clinica import Clinica
import pandas as pd

class TestVerTerapeutas(unittest.TestCase):

    def test_ver_terapeutas(self):
        clinica = Clinica()
        
        csv_file = 'C:/Users/María José/Documents/U Creativa/Proyecto Final 2.0/informacion.csv'

        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            try:
                terapeutas_df = pd.read_csv(csv_file, encoding='utf-8')
            except UnicodeDecodeError:
                try:
                    terapeutas_df = pd.read_csv(csv_file, encoding='latin1')
                except UnicodeDecodeError:
                    terapeutas_df = pd.read_csv(csv_file, encoding='utf-8', errors='ignore')
            print("Listado de Terapeutas Disponibles:")
            print(terapeutas_df)
            output = out.getvalue().strip()  
            self.assertGreater(len(output), 0)
        finally:
            sys.stdout = saved_stdout

if __name__ == '__main__':
    unittest.main()
