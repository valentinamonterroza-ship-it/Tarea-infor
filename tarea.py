
class Conjun:

    def __init__(self, nombre, cedula, genero):
        self._nombre = nombre
        self._cedula = cedula
        self._genero = genero

    # GETTERS
    def get_nombre(self):
        return self._nombre

    def get_cedula(self):
        return self._cedula

    def get_genero(self):
        return self._genero

    # SETTERS
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cedula(self, cedula):
        self._cedula = cedula

    def set_genero(self, genero):
        self._genero = genero

    def __str__(self):
        return f"Nombre: {self._nombre}, Cedula: {self._cedula}, Genero: {self._genero}"



class Paciente(Conjun):

    def __init__(self, nombre, cedula, genero, servicio):
        super().__init__(nombre, cedula, genero)
        self._servicio = servicio

    # GETTER
    def get_servicio(self):
        return self._servicio

    # SETTER
    def set_servicio(self, servicio):
        self._servicio = servicio

    def __str__(self):
        return f"{super().__str__()}, Servicio: {self._servicio}"



class SistemaHospital:

    def __init__(self):
        self._pacientes = []

    # Verificar si existe paciente
    def existe_paciente(self, cedula):

        for paciente in self._pacientes:
            if paciente.get_cedula() == cedula:
                return True

        return False


    # Agregar paciente
    def agregar_paciente(self, paciente):

        if self.existe_paciente(paciente.get_cedula()):
            return False

        self._pacientes.append(paciente)
        return True


    # Buscar paciente
    def buscar_paciente(self, cedula):

        for paciente in self._pacientes:
            if paciente.get_cedula() == cedula:
                return paciente

        return None


    # Cantidad de pacientes
    def cantidad_pacientes(self):
        return len(self._pacientes)


    # Mostrar todos
    def mostrar_pacientes(self):

        if len(self._pacientes) == 0:
            print("No hay pacientes registrados")
        else:
            for paciente in self._pacientes:
                print(paciente)


# =========================
# FUNCION PRINCIPAL
# =========================

def main():

    sistema = SistemaHospital()

    while True:

        print("\n-------- SISTEMA HOSPITAL --------")
        print("1. Ingresar paciente nuevo")
        print("2. Ver datos de paciente")
        print("3. Ver número de pacientes")
        print("4. Ver todos los pacientes")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        # OPCION 1
        if opcion == "1":

            nombre = input("Ingrese nombre: ")
            cedula = input("Ingrese cedula: ")
            genero = input("Ingrese genero: ")
            servicio = input("Ingrese servicio: ")

            paciente = Paciente(nombre, cedula, genero, servicio)

            if sistema.agregar_paciente(paciente):
                print("Paciente agregado correctamente")
            else:
                print("Error: ya existe un paciente con esa cedula")


        # OPCION 2
        elif opcion == "2":

            cedula = input("Ingrese la cedula: ")

            paciente = sistema.buscar_paciente(cedula)

            if paciente != None:
                print("\nPaciente encontrado:")
                print(paciente)
            else:
                print("Paciente no existe")


        # OPCION 3
        elif opcion == "3":

            print("Cantidad de pacientes:",
                  sistema.cantidad_pacientes())


        # OPCION 4
        elif opcion == "4":

            sistema.mostrar_pacientes()


        # OPCION 5
        elif opcion == "5":

            print("Gracias por usar el sistema")
            break


        else:
            print("Opcion invalida")


main()
