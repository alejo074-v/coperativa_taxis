from taxi import Taxi
from conductor import Conductor
from propietario import Propietario
from os import system

taxis = range(4)

class Cooperativa:
    def __init__(self, taxis):
        self._taxis = taxis
    
    
    def menu():
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
            Cooperativa.ingresar_datos()
            menu()
        if opcion == 2:
            Cooperativa.buscar_taxi_propietario()
            menu()
        if opcion == 3:
            Cooperativa.total_pagar_conductore()
            menu()
        if opcion == 4:
            Cooperativa.datos_taxi()
            menu()
        if opcion == 5:
            Cooperativa.salario_conductor()
            menu()
        if opcion == 6:
            SystemExit

    def ingresar_datos():
        print("Ingrese el nombre del propietario abajo")
        nombreC = str(input())

        print("Ingrese la cédula del propietario abajo")
        cedulaC = int(input())

        print("Ingrese el teléfono del propietario abajo")
        telefonoC = int(input())
        # Objeto tipo propietario 
        propietarioC = propietario.Propietario(cedula=cedulaC, nombre=nombreC, telefono=telefonoC)

        print("Ingrese el nombre del conductor abajo")
        nombreC = str(input())

        print("Ingrese la cédula del conductor abajo")
        cedulaC = int(input())

        print("Ingrese el salário del conductor abajo")
        salarioC = int(input())
        # Objeto tipo conductor
        conductorC = conductor.Conductor(nombre=nombreC, cedula=cedulaC, salario=salarioC)

        print("Ingresa la marca del auto abajo")
        marcaC = str(input())

        print("Ingrese el modelo del auto abajo")
        modeloC = int(input())

        print("Ingrese la placa del auto abajo")
        placaC = int(input())

        print("Ingrese el tamaño de motor del auto abajo")
        tamaño_motorC = int(input())
        # Objeto tipo taxi

        for i in taxi:
            taxis = taxi.Taxi(marca=marcaC, modelo=modeloC, placa=placaC, tamañoMotor=tamaño_motorC, propietarioT=propietarioC, conductorT=conductorC)

    def buscar_taxi_propietario():
        pass

    def total_pagar_conductore():
        pass

    def datos_taxi():
        pass

    def salario_conductor():
        pass



if __name__ == "__main__":
    Cooperativa.menu()


