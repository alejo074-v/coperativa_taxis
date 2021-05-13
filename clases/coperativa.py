import taxi, conductor, propietario

class Cooperativa:

    def __init__(self):
        self._taxis = []

    def menu(self):
        opcion = 0

        while opcion < 1 or opcion > 6:
            print("     Menu Principal De Gestion de la cooperativa")
            print("[ 1 ]. Ingresar datos.")
            print("[ 2 ]. Buscar taxis de propietario.")
            print("[ 3 ]. Determinar el total a pagar de los conductores.")
            print("[ 4 ]. Identificar datos de un taxi.")
            print("[ 5 ]. Buscar salario de conductor.")
            print("[ 6 ]. Salir.")
            print("Ingresa la opcion abajo")
            opcion = int(input())

        if opcion == 1:
            self.ingresarDatos()
            self.menu()
        if opcion == 2:
            self.buscarTaxiPropietario()
            self.menu()
        if opcion == 3:
            self.totalPagarConductores()
            self.menu()
        if opcion == 4:
            self.datosTaxi()
            self.menu()
        if opcion == 5:
            self.salarioConductor()
            self.menu()
        if opcion == 6:
            print("Fin del programa")

    def ingresarDatos(self):
        print("Ingrese el nombre del propietario:")
        nombrePropietario = str(input())
        print("Ingrese el cedula del propietario:")
        cedulaPropietario = int(input())
        print("Ingrese el telefono del propietario:")
        telefonoPropietario = int(input())
        prop = propietario.Propietario(cedula = cedulaPropietario, nombre = nombrePropietario, telefono =telefonoPropietario)


        print("Ingrese el nombre del conductor:")
        nombreConductor = str(input())
        print("Ingrese la cedula del conductor:")
        cedulaConductor = int(input())
        print("Ingrese el salario del conductor:")
        salarioConductor = int(input())
        cond = conductor.Conductor(cedula = cedulaConductor, nombre = nombreConductor, salario = salarioConductor)

        print("Ingrese la marca del taxi:")
        marca = str(input())
        print("Ingrese el modelo del taxi:")
        modelo = str(input())
        print("Ingrese la placa del taxi:")
        placa = str(input())
        print("Ingrese el tamaño del motor del taxi:")
        tamMotor = float(input())

        taxiO = taxi.Taxi(marca = marca, modelo = modelo, placa = placa, tamMotor = tamMotor, propietariot = prop, conductort = cond)
        self._taxis.append(taxiO)

    def buscarTaxiPropietario(self):
        noEncontrado = True
        print("Ingrese la cedula del propietario:")
        cedula = int(input())
        for i in self._taxis:
            if i.propietario.cedula == cedula:
                print(i.toString())
                noEncontrado = False
                break
            pass
        if noEncontrado:
            print("Cedula no encontrada")

    def totalPagarConductores(self):
        totalSalarios = 0.0
        for i in self._taxis:
            totalSalarios += i.conductor.salario
            pass
        print("total a pagar a los conductores es: ", totalSalarios, "$")

    def datosTaxi(self):
        opcion = 0

        while opcion < 1 or opcion > 6:
            print("[ 1 ]. Buscar por placa.")
            print("[ 2 ]. Buscar Por Cedula.")
            print("[ 3 ]. Salir.")
            print("Ingresa la opcion abajo")
            opcion = int(input())

        if opcion == 1:
            noEncontrado = True
            print("Ingrese la placa:")
            placa = str(input())
            for i in self._taxis:
                if i.placa == placa:
                    print(i.toString())
                    noEncontrado = False
                    break
                pass
            if noEncontrado:
                print("Placa no encontrada")
        if opcion == 2:
            print("vacio")
        if opcion == 3:
            self.menu()

    def salarioConductor(self):
        noEncontrado = True
        print("Ingrese la cedula:")
        cedula = int(input())
        for i in self._taxis:
            if i.conductor.cedula == cedula:
                print(i.conductor.salario)
                noEncontrado = False
                break
            pass
        if noEncontrado:
            print("Cedula no encontrada")





if __name__ == "__main__":
    coo = Cooperativa()
    coo.menu()
