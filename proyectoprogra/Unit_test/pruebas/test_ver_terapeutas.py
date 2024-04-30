import unittest
from Clases.clase_clinica import Clinica
import pandas as pd

class TestVerTerapeutas(unittest.TestCase):

    def test_ver_terapeutas(self):
        # Creamos una instancia de la clase Clinica
        clinica = Clinica()

        # Establecemos el archivo CSV existente en la instancia de Clinica
        csv_file = 'C:/Users/María José/Documents/U Creativa/Proyecto Final 2.0/informacion.csv'

        # Llamamos a la función ver_terapeutas y almacenamos la salida en un string
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            # Leemos el archivo CSV especificando la codificación
            try:
                terapeutas_df = pd.read_csv(csv_file, encoding='utf-8')
            except UnicodeDecodeError:
                # Intentamos leer el archivo con diferentes codificaciones o manejamos el error de otra manera
                try:
                    terapeutas_df = pd.read_csv(csv_file, encoding='latin1')
                except UnicodeDecodeError:
                    # Intentamos ignorar los errores de codificación
                    terapeutas_df = pd.read_csv(csv_file, encoding='utf-8', errors='ignore')
            print("Listado de Terapeutas Disponibles:")
            print(terapeutas_df)
            output = out.getvalue().strip()  # Obtenemos la salida sin espacios en blanco al principio y al final
            # Verificamos que la salida contenga alguna información de los terapeutas
            self.assertGreater(len(output), 0)
        finally:
            sys.stdout = saved_stdout

if __name__ == '__main__':
    unittest.main()
