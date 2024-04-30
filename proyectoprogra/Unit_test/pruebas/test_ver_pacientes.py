import unittest
from Clases.clase_clinica import Clinica

class TestVerPacientes(unittest.TestCase):

    def test_ver_pacientes(self):
        # Creamos una instancia de la clase Clinica
        clinica = Clinica()

        # Establecemos el archivo CSV existente en la instancia de Clinica
        clinica.pacientes_csv = 'C:/Users/María José/Documents/U Creativa/Proyecto Final 2.0/pacientes.csv'

        # Llamamos a la función ver_pacientes y almacenamos la salida en un string
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            clinica.ver_pacientes()
            output = out.getvalue().strip()  # Obtenemos la salida sin espacios en blanco al principio y al final
            # Verificamos que la salida contenga alguna información de los pacientes
            self.assertGreater(len(output), 0)
        finally:
            sys.stdout = saved_stdout

if __name__ == '__main__':
    unittest.main()
