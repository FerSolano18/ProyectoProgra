import unittest
import os
from Clases.clase_clinica import Clinica

class TestGuardarPacientes(unittest.TestCase):

    def setUp(self):
        self.clinica = Clinica()
        self.csv_path = 'C:/Users/María José/Documents/U Creativa/Proyecto Final 2.0/Unit_test/pruebas/test_pacientes.csv'
        with open(self.csv_path, 'w') as file:
            file.write("Nombre,Apellido,Cedula,Telefono,Correo,Direccion,Terapeuta,Razon,Notas,Fecha,Metodo de Pago\n")
            file.write("Lili,Cortes,1234567890,123456789,lili@gmail.com,Orosi,Dr. Solano,Dolor nervio,Dolor en el nervio de una costilla,2024-05-01,Efectivo\n")

    def test_guardar_pacientes_creacion_archivo(self):

        self.assertTrue(os.path.isfile(self.csv_path))
        with open(self.csv_path, 'r') as file:
            csv_data = file.read()
            self.assertIn("Nombre,Apellido,Cedula,Telefono,Correo,Direccion,Terapeuta,Razon,Notas,Fecha,Metodo de Pago", csv_data)

    def test_guardar_pacientes_agregar_datos(self):

        self.assertTrue(os.path.isfile(self.csv_path))
        with open(self.csv_path, 'r') as file:
            csv_data = file.read()
            self.assertIn("Lili,Cortes,1234567890,123456789,lili@gmail.com,Orosi,Dr. Solano,Dolor nervio,Dolor en el nervio de una costilla,2024-05-01,Efectivo", csv_data)

if __name__ == '__main__':
    unittest.main()
