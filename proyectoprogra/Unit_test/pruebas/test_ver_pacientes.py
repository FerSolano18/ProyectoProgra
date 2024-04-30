import unittest
from Clases.clase_clinica import Clinica

class TestVerPacientes(unittest.TestCase):

    def test_ver_pacientes(self):
        clinica = Clinica()

        clinica.pacientes_csv = 'C:/Users/María José/Documents/U Creativa/Proyecto Final 2.0/pacientes.csv'

        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            clinica.ver_pacientes()
            output = out.getvalue().strip()  
            self.assertGreater(len(output), 0)
        finally:
            sys.stdout = saved_stdout

if __name__ == '__main__':
    unittest.main()
