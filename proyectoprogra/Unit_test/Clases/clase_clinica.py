import pandas as pd

class Clinica:
    def __init__(self):
        self.informacion_csv = 'informacion.csv'
        self.pacientes_csv = 'pacientes.csv'
        self.terapeutas_disponibles = pd.DataFrame(columns=['Nombre', 'Apellido', 'Día', 'Fecha', 'Hora', 'Sede', 'Especialidad', 'Tarifa'])
        self.password = 'mypassword'

    def guardar_terapeutas(self):
        self.terapeutas_disponibles.to_csv(self.informacion_csv, mode='a', index=False, header=False if not pd.read_csv(self.informacion_csv).empty else True)

    def guardar_pacientes(self, datos_paciente):
        paciente_nuevo = pd.DataFrame(datos_paciente)
        paciente_nuevo.to_csv(self.pacientes_csv, mode='a', index=False, header=False if not pd.read_csv(self.pacientes_csv).empty else True) 
        
    def ver_terapeutas(self):
        terapeutas_df = pd.read_csv(self.informacion_csv)
        print("Listado de Terapeutas Disponibles:")
        print(terapeutas_df)

    def ver_pacientes(self):
        pacientes_df = pd.read_csv(self.pacientes_csv)
        print("Listado de Pacientes Registrados:")
        print(pacientes_df)

clinica = Clinica()

# Menú principal para determinar el nivel de acceso
while True:
    print("\nEscoja el tipo de acceso mediante la selección del número correcto")
    print("1 - Acceso de Servicio al Cliente")
    print("2 - Acceso de Terapeuta")
    print("3 - Salir")
    acceso = int(input("Seleccione el tipo de acceso: "))

    # Menú Servicio al cliente
    if acceso == 1:
        print("\nMenu de Servicio al Cliente:")
        print("1 - Ver la disponibilidad de terapeutas")
        print("2 - Agregar un terapeuta disponible")
        print("3 - Ver listado de pacientes")
        print("4 - Salir")
        opcion = int(input("Seleccione la opción que describe cómo desea proceder: "))

        if opcion == 1:
            clinica.ver_terapeutas()
        elif opcion == 2:
            nombre = input("Ingrese el nombre del terapeuta: ")
            apellido = input("Ingrese el apellido del terapeuta: ")
            dia = input("Ingrese el día de disponibilidad: ")
            fecha = input("Ingrese la fecha de disponibilidad: ")
            hora = input("Ingrese la hora de disponibilidad: ")
            sede = input("Ingrese la sede de trabajo: ")
            especialidad = input("Ingrese la especialidad: ")
            tarifa = input("Ingrese la tarifa del terapeuta: ")
            nuevo_terapeuta = {
                'Nombre': nombre,
                'Apellido': apellido,
                'Dia': dia,
                'Fecha': fecha,
                'Hora': hora,
                'Sede': sede,
                'Especialidad': especialidad,
                'Tarifa': tarifa
            }
            clinica.terapeutas_disponibles = pd.concat([clinica.terapeutas_disponibles, pd.DataFrame([nuevo_terapeuta])], ignore_index=True)
            clinica.guardar_terapeutas()
        elif opcion == 3:
            clinica.ver_pacientes()
        elif opcion == 4:
            break

    # Menú para terapeutas
    elif acceso == 2:
        # Solicitar la contraseña
        password_input = input("Ingrese la contraseña: ")
        if password_input == clinica.password:  # revisar si la contraseña es correcta
            print("Contraseña correcta. Acceso permitido.")
            print("Que desea hacer?")
            print("1 - Ver paciente")
            print("2 - Agregar información de paciente")
            print("3 - Salir")
            opcion2 = int(input("Seleccione la opción que describe cómo desea proseguir: "))
            if opcion2 == 1:
                clinica.ver_pacientes()
            elif opcion2 == 2:
                datos_paciente = {
                    'Nombre': [input("Ingrese el nombre del paciente: ")],
                    'Apellidos': [input("Ingrese los apellidos del paciente: ")],
                    'Cedula': [input("Ingrese la cédula del paciente: ")],
                    'Telefono': [input("Ingrese el teléfono del paciente: ")],
                    'Correo': [input("Ingrese el correo del paciente: ")],
                    'Direccion': [input("Ingrese la dirección del paciente: ")],
                    'Terapeuta': [input("Ingrese el terapeuta del paciente: ")],
                    'Razon': [input("Ingrese el tipo de consulta del paciente: ")],
                    'Notas': [input("Ingrese las notas del paciente: ")],
                    'Fecha': [input("Ingrese la fecha de la consulta: ")],
                    'Metodo de Pago': [input("Ingrese el método de pago: ")]
               }
                clinica.guardar_pacientes(datos_paciente)
            elif opcion2 == 3:
                break
        else:
            print("Contraseña incorrecta. Acceso denegado.")

    elif acceso == 3:
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

