class Conjun:

    def __init__(self, nombre, cedula, genero):
        self._nombre = nombre
        self._cedula = cedula
        self._genero = genero

    def get_nombre(self):
        return self._nombre

    def get_cedula(self):
        return self._cedula

    def get_genero(self):
        return self._genero

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cedula(self, cedula):
        self._cedula = cedula

    def set_genero(self, genero):
        self._genero = genero

    def __str__(self):
        return f"El nombre es: {self._nombre}, con cedula: {self._cedula} y Genero: {self._genero}"


class Paciente(Conjun):

    def __init__(self, nombre, cedula, genero, servicio):
        super().__init__(nombre, cedula, genero)
        self._servicio = servicio

    def get_servicio(self):
        return self._servicio

    def set_servicio(self, servicio):
        self._servicio = servicio

    def __str__(self):
        return f"{super().__str__()}, Servicio: {self._servicio}"


class Enfermera(Conjun):

    def __init__(self, nombre, cedula, genero, turno, rango):
        super().__init__(nombre, cedula, genero)
        self._turno = turno
        self._rango = rango

    def get_turno(self):
        return self._turno

    def get_rango(self):
        return self._rango

    def set_turno(self, turno):
        self._turno = turno

    def set_rango(self, rango):
        self._rango = rango

    def __str__(self):
        return f"{super().__str__()}, Turno: {self._turno}, Rango: {self._rango}"


class Medico(Conjun):

    def __init__(self, nombre, cedula, genero, turno, especialidad):
        super().__init__(nombre, cedula, genero)
        self._turno = turno
        self._especialidad = especialidad

    def get_turno(self):
        return self._turno

    def get_especialidad(self):
        return self._especialidad

    def set_turno(self, turno):
        self._turno = turno

    def set_especialidad(self, especialidad):
        self._especialidad = especialidad

    def __str__(self):
        return f"{super().__str__()}, Turno: {self._turno}, Especialidad: {self._especialidad}"


class Hospital:

    def __init__(self):
        self.pacientes = []
        self.enfermeras = []
        self.medicos = []

    def agregar_paciente(self, paciente):

        for p in self.pacientes:
            if p.get_cedula() == paciente.get_cedula():
                return False

        self.pacientes.append(paciente)
        return True


    def agregar_enfermera(self, enfermera):
        self.enfermeras.append(enfermera)

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def buscar_paciente_por_cedula(self, cedula):
        for paciente in self.pacientes:
            if paciente.get_cedula() == cedula:
                return paciente
        return None

    def numero_pacientes(self):
        return len(self.pacientes)

    def numero_enfermeras(self):
        return len(self.enfermeras)

    def numero_medicos(self):
        return len(self.medicos)

    def almacenar_todo(self):

        print("- PACIENTES -")
        for p in self.pacientes:
            print(p)

        print("\n- ENFERMERAS -")
        for e in self.enfermeras:
            print(e)

        print("\n-MEDICOS -")
        for m in self.medicos:
            print(m)


def main():

    sistema = Hospital()

    while True:

        print("\n---- SISTEMA HOSPITAL ----")
        print("1. Ingresar paciente nuevo")
        print("2. Ver datos de paciente existente")
        print("3. Ver numero de pacientes")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            nombre = input("Ingrese nombre: ")
            cedula = input("Ingrese cedula: ")
            genero = input("Ingrese genero: ")
            servicio = input("Ingrese servicio: ")

            paciente = Paciente(nombre, cedula, genero, servicio)

            if sistema.agregar_paciente(paciente):
                print("Paciente agregado correctamente al sistema")
            else:
                print("Error: ya existe un paciente con esa cedula")


        elif opcion == "2":

            cedula = input("Ingrese la cedula del paciente: ")

            paciente = sistema.buscar_paciente_por_cedula(cedula)

            if paciente != None:
                print("\nPaciente encontrado:")
                print(paciente)
            else:
                print("El paciente no existe")


        elif opcion == "3":

            print("Numero de pacientes:", sistema.numero_pacientes())


        elif opcion == "4":

            print("Gracias por usar el sistema, saliendo...")
            break

        else:
            print("Opcion invalida")


main()


