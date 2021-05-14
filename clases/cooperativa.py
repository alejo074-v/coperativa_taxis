from taxi import Taxi
from conductor import Conductor
from propietario import Propietario
from os import system


class Cooperativa:
    def __init__(self):
        self._taxis = []

    def menu(self):
        opcion = 0
        while opcion < 1 or opcion > 6:
            system("cls")
            print("     Menu Principal De Gestion de la cooperativa")
            print("[ 1 ]. Ingresar datos.")
            print("[ 2 ]. Buscar taxis de propietario.")
            print("[ 3 ]. Determinar el total a pagar de los conductores.")
            print("[ 4 ]. Identificar datos de un taxi.")
            print("[ 5 ]. Buscar salario de conductor.")
            print("[ 6 ]. Salir.")
            print("Ingresa la opcion abajo")

            try:
                opcion = int(input())
            except:
                self.menu()

        if opcion == 1:
            self.ingresarDatos()
            self.menu()
        if opcion == 6:
            print("Fin del programa")
            return

        if len(self._taxis) == 0:
            print("No se han ingresado datos aún")
        else:
            if opcion == 2:
                self.buscarTaxiPropietario()
            if opcion == 3:
                self.totalPagarConductores()
            if opcion == 4:
                self.datosTaxi()
            if opcion == 5:
                self.salarioConductor()

        input("Press Enter to continue...")
        self.menu()


    def ingresarDatos(self):
        system('cls')
        print("Ingrese el nombre del propietario:")
        nombrePropietario = str(input())
        system('cls')
        print("Ingrese el cedula del propietario:")
        cedulaPropietario = int(input())
        system('cls')
        print("Ingrese el telefono del propietario:")
        telefonoPropietario = int(input())
        system('cls')
        prop = Propietario(cedula = cedulaPropietario, nombre = nombrePropietario, telefono =telefonoPropietario)


        print("Ingrese el nombre del conductor:")
        nombreConductor = str(input())
        system('cls')
        print("Ingrese la cedula del conductor:")
        cedulaConductor = int(input())
        system('cls')
        print("Ingrese el salario del conductor:")
        salarioConductor = int(input())
        system('cls')
        cond = Conductor(cedula = cedulaConductor, nombre = nombreConductor, salario = salarioConductor)

        print("Ingrese la marca del taxi:")
        marca = str(input())
        system('cls')
        print("Ingrese el modelo del taxi:")
        modelo = str(input())
        system('cls')
        print("Ingrese la placa del taxi:")
        placa = str(input())
        system('cls')
        print("Ingrese el tamaño del motor del taxi:")
        tamMotor = float(input())
        system('cls')

        taxiO = Taxi(marca = marca, modelo = modelo, placa = placa, tamMotor = tamMotor, propietarioT = prop, conductorT = cond)
        self._taxis.append(taxiO)

        # Objeto tipo taxi
        # change = False
        # i = 0
        # while i < len(taxis):
        #     if taxis[i] == 0:
        #         taxis[i] = Taxi(marca=marcaC, modelo=modeloC, placa=placaC, tamañoMotor=tamaño_motorC, propietarioT=propietarioC, conductorT=conductorC)
        #         change = True
        #         break
        #     i = i + 1
        #
        # if change == False:
        #     print("No se pueden ingresar más datos")

    def buscarTaxiPropietario(self):
        system('cls')

        noEncontrado = True
        print("Ingrese la cedula del propietario:")
        cedula = int(input())
        for i in self._taxis:
            if i._propietarioT.cedula == cedula:
                print(i.toString())
                noEncontrado = False
                break
            pass
        if noEncontrado:
            print("Cedula no encontrada")

    def totalPagarConductores(self):
        system('cls')
        totalSalarios = 0.0
        for i in self._taxis:
            totalSalarios += i._conductorT.salario
            pass
        print("total a pagar a los conductores es: ", totalSalarios, "$")

    def datosTaxi(self):
        system('cls')
        opcion = 0

        while opcion < 1 or opcion > 3:
            print("[ 1 ]. Buscar por placa.")
            print("[ 2 ]. Buscar Por Cedula.")
            print("[ 3 ]. Salir.")
            print("Ingresa la opcion abajo")

            try:
                opcion = int(input())
            except:
                self.datosTaxi()

        if opcion == 1:
            noEncontrado = True
            print("Ingrese la placa:")
            placa = str(input())
            for i in self._taxis:
                if i.placa == placa:
                    print(i.taxi_to_string())
                    noEncontrado = False
                    break
                pass
            if noEncontrado:
                print("Placa no encontrada")
        if opcion == 2:
            system('cls')
            if len(self._taxis) == 0:
                print("No se han ingresado datos aún")
            else:
                noEncontrado = True
                print("Ingrese la cedula del propietario:")
                cedula = int(input())
                for i in self._taxis:
                    if i._propietarioT.cedula == cedula or i._conductorT.cedula == cedula:
                        print(i.taxi_to_string())
                        noEncontrado = False
                        break
                    pass
                if noEncontrado:
                    print("Cedula no encontrada")
        if opcion == 3:
            self.menu()

    def salarioConductor(self):
        system('cls')
        noEncontrado = True
        print("Ingrese la cedula:")
        cedula = int(input())
        for i in self._taxis:
            if i._conductorT.cedula == cedula:
                print(i._conductorT.salario)
                noEncontrado = False
                break
            pass
        if noEncontrado:
            print("Cedula no encontrada")

if __name__ == "__main__":
    coo = Cooperativa()
    coo.menu()
