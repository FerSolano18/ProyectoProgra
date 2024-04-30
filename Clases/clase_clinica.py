import pandas as pd

# Clase clínica
class Clinica:
    def __init__(self):
        self.informacion_csv = 'informacion.csv'
        self.pacientes_csv = 'pacientes.csv'
        self.terapeutas_disponibles = pd.DataFrame(columns=['Nombre', 'Apellido', 'Día', 'Fecha', 'Hora', 'Sede', 'Especialidad', 'Tarifa'])
        self.password = 'mypassword'

    def guardar_terapeutas(self):
        self.terapeutas_disponibles.to_csv(self.informacion_csv, mode='a', index=False, header=not pd.read_csv(self.informacion_csv).empty)

    def guardar_pacientes(self):
        datos_paciente = {
            'Nombre': [input("Ingrese el nombre del paciente: ")],
            'Apellidos': [input("Ingrese los apellidos del paciente: ")],
            'Cedula': [input("Ingrese la cédula del paciente: ")],
            'Telefono': [input("Ingrese el teléfono del paciente: ")],
            'Correo': [input("Ingrese el correo del paciente: ")],
            'Direccion': [input("Ingrese la dirección del paciente: ")],
            'Terapeuta': [input("Ingrese el terapeuta del paciente: ")],
            'Consulta': [input("Ingrese el tipo de consulta del paciente: ")],
            'Notas': [input("Ingrese las notas del paciente: ")],
            'Fecha': [input("Ingrese la fecha de la consulta: ")],
            'Método de Pago': [input("Ingrese el método de pago: ")]
        }
        paciente_nuevo = pd.DataFrame(datos_paciente)
        paciente_nuevo.to_csv(self.pacientes_csv, mode='a', index=False, header=not pd.read_csv(self.pacientes_csv).empty)

        print("Datos de paciente ingresados correctamente.")

    def ver_terapeutas(self):
        terapeutas_df = pd.read_csv(self.informacion_csv)
        print("Listado de Terapeutas Disponibles:")
        print(terapeutas_df)

    def ver_pacientes(self):
        pacientes_df = pd.read_csv(self.pacientes_csv)
        print("Listado de Pacientes Registrados:")
        print(pacientes_df)

clinica = Clinica()