from taxi import Taxi
from conductor import Conductor
from propietario import Propietario
from os import system


taxis = [0]*4

class Cooperativa:
    def __init__():
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

    # Ingresar datos de cada taxi
    def ingresar_datos():
        system('cls')
        print("Ingrese el nombre del propietario abajo")
        nombreC = str(input())
        system('cls')

        print("Ingrese la cédula del propietario abajo")
        cedulaC = int(input())
        system('cls')

        print("Ingrese el teléfono del propietario abajo")
        telefonoC = int(input())
        # Objeto tipo propietario 
        propietarioC = Propietario(cedula=cedulaC, nombre=nombreC, telefono=telefonoC)
        system('cls')

        print("Ingrese el nombre del conductor abajo")
        nombreC = str(input())
        system('cls')

        print("Ingrese la cédula del conductor abajo")
        cedulaC = int(input())
        system('cls')

        print("Ingrese el salário del conductor abajo")
        salarioC = int(input())
        # Objeto tipo conductor
        conductorC = Conductor(nombre=nombreC, cedula=cedulaC, salario=salarioC)
        system('cls')

        print("Ingresa la marca del auto abajo")
        marcaC = str(input())
        system('cls')

        print("Ingrese el modelo del auto abajo")
        modeloC = int(input())
        system('cls')

        print("Ingrese la placa del auto abajo")
        placaC = str(input())
        system('cls')

        print("Ingrese el tamaño de motor del auto abajo")
        tamaño_motorC = int(input())
        system('cls')

        # Objeto tipo taxi

        i = 0
        while i < len(taxis):
            if taxis[i] == 0:
                i = Taxi(marca=marcaC, modelo=modeloC, placa=placaC, tamañoMotor=tamaño_motorC, propietarioT=propietarioC, conductorT=conductorC)
            elif i == len(taxis) and i != 0:
                print("La base de datos está llena así que no podemos guardar más taxis")
            i = i + 1

        # Objeto tipo taxi
        change = False
        i = 0
        while i < len(taxis):
            if taxis[i] == 0:
                taxis[i] = Taxi(marca="Tesla", modelo=2000, placa="UTF-8", tamañoMotor=200, propietarioT=propietarioC, conductorT=conductorC)
                change = True
                break
            i = i+1
        
        if change == False:
            print("No se pueden ingresar más datos")

    # Buscar el propietario de algún taxi por medio de la cédula 
    def buscar_taxi_propietario():
        system('cls')
        print("Ingresa la cédula del propietario abajo")
        cedula = int(input())
<<<<<<< HEAD

        let = False
        i = 0
        while i < len(taxis):
            if taxis[i]._propietarioT.cedula == cedula:
                print(taxi[i].toString())
                let = True
                break
        
        if let == False:
            print("Cédula no encontrada")
            

    def total_pagar_conductore():
        pass

    def datos_taxi():
        pass

    def salario_conductor():
        pass



if __name__ == "__main__":
    system('cls')
    Cooperativa.__init__()


