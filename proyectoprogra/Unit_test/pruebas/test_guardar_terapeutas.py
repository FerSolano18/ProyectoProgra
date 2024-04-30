import unittest
import pandas as pd
import os
from Clases.clase_clinica import Clinica

class TestGuardarTerapeutas(unittest.TestCase):

    def setUp(self):
        self.clinica = Clinica()
        self.csv_path = 'C:/Users/María José/Documents/U Creativa/Proyecto Final 2.0/Unit_test/pruebas/test_informacion.csv'

    def test_guardar_terapeutas_no_existente(self):
        self.clinica.guardar_terapeutas()

        self.assertTrue(os.path.isfile(self.csv_path))
        with open(self.csv_path, 'r') as file:
            csv_data = file.read()
            self.assertIn("Nombre,Apellido,Dia,Fecha,Hora,Sede,Especialidad,Tarifa\n", csv_data)

    def test_guardar_terapeutas_existente(self):
        with open(self.csv_path, 'w') as file:
            file.write("Nombre,Apellido,Dia,Fecha,Hora,Sede,Especialidad,Tarifa\n")
            file.write("Maria,Solano,Lunes,2024-05-03,09:00,Cartago,Fisioterapia,25000\n")

        self.assertTrue(os.path.isfile(self.csv_path))

        self.clinica.guardar_terapeutas()

        self.assertTrue(os.path.isfile(self.csv_path))
        with open(self.csv_path, 'r') as file:
            csv_data = file.read()
            self.assertIn("Nombre,Apellido,Dia,Fecha,Hora,Sede,Especialidad,Tarifa\n", csv_data)
            self.assertIn("Maria,Solano,Lunes,2024-05-03,09:00,Cartago,Fisioterapia,25000\n", csv_data)

if __name__ == '__main__':
    unittest.main()
