from taxi import Taxi
from conductor import Conductor
from propietario import Propietario
from os import system

taxis = range(4)


class Cooperativa:
    def __init__(self, taxis):
        self._taxis = taxis
    
    
    def menu():
        taxis = range(4)
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
            Cooperativa.menu()
        if opcion == 2:
            Cooperativa.buscar_taxi_propietario()
            Cooperativa.menu()
        if opcion == 3:
            Cooperativa.total_pagar_conductore()
            Cooperativa.menu()
        if opcion == 4:
            Cooperativa.datos_taxi()
            Cooperativa.menu()
        if opcion == 5:
            Cooperativa.salario_conductor()
            Cooperativa.menu()
        if opcion == 6:
            SystemExit

    # Obtener datos de cada taxi
    def ingresar_datos():
        system('cls')
        print("Ingrese el nombre del propietario abajo")
        nombre = str(input())
        system('cls')

        print("Ingrese la cédula del propietario abajo")
        cedula = int(input())
        system('cls')

        print("Ingrese el teléfono del propietario abajo")
        telefono = int(input())
        # Objeto tipo propietario 
        system('cls')
        propietario = Propietario(cedula=cedula, nombre=nombre, telefono=telefono)
        print(propietario.toString())

        print("Ingrese el nombre del conductor abajo")
        nombre = str(input())
        system('cls')

        print("Ingrese la cédula del conductor abajo")
        cedula = int(input())
        system('cls')

        print("Ingrese el salário del conductor abajo")
        salario = int(input())
        system('cls')
        # Objeto tipo conductor
        conductor = Conductor(nombre=nombre, cedula=cedula, salario=salario)
        print(conductor.toString())

        print("Ingresa la marca del auto abajo")
        marca = str(input())
        system('cls')

        print("Ingrese el modelo del auto abajo")
        modelo = int(input())
        system('cls')

        print("Ingrese la placa del auto abajo")
        placa = str(input())
        system('cls')

        print("Ingrese el tamaño de motor del auto abajo")
        tamaño_motor = int(input())
        system('cls')
        # Objeto tipo taxi

        for i in taxis:
            i = Taxi(marca=marca, modelo=modelo, placa=placa, tamañoMotor=tamaño_motor, propietarioT=propietario, conductorT=conductor)

    # Buscar referencias de automovil por medio de celula del propietario
    def buscar_taxi_propietario():
        print("Ingrese la cédula abajo")
        cedula = int(input())
        for i in range(len(taxis)):
            if cedula == "":
                print("Cedula no encontrada")
                break
            else:
                if taxis[i].cedula == cedula:
                    print(taxis[i].toString())
            i+=1
        
            


    def total_pagar_conductore():
        total_salario = 0
        for i in range(len(taxis)):
            total_salario += taxis[i].salario
            i+=1
        print("El total a pagar a los conductores es: $" + total_salario)

    def datos_taxi():
        

    def salario_conductor():
        pass



if __name__ == "__main__":
    Cooperativa.menu()


