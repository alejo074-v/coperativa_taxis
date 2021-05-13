from taxi import Taxi
from conductor import Conductor
from propietario import Propietario
from os import system


taxis = [0]*4

class Cooperativa:
    def __init__():
        opcion = 0
        while opcion != '1' and opcion != '2' and opcion != '3' and opcion != '4' \
            and opcion != '5' and opcion != '6':
            print("     Menu Principal De Gestion de la cooperativa")
            print("[ 1 ]. Ingresar datos.")
            print("[ 2 ]. Buscar taxis de propietario.")
            print("[ 3 ]. Determinar el total a pagar de los conductores.")
            print("[ 4 ]. Identificar datos de un taxi.")
            print("[ 5 ]. Buscar salario de conductor.")
            print("[ 6 ]. Salir.")
            print("Ingresa la opcion abajo")
            opcion = str(input())




        if opcion == '1':
            Cooperativa.ingresar_datos()
            Cooperativa.__init__()
        if opcion == '2':
            Cooperativa.buscar_taxi_propietario()
            Cooperativa.__init__()
        if opcion == '3':
            Cooperativa.total_pagar_conductores()
            Cooperativa.__init__()
        if opcion == '4':
            Cooperativa.datos_taxi()
            Cooperativa.__init__()
        if opcion == '5':
            Cooperativa.salario_conductor()
            Cooperativa.__init__()
        if opcion == '6':
            system('cls')
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
        change = False
        i = 0
        while i < len(taxis):
            if taxis[i] == 0:
                taxis[i] = Taxi(marca=marcaC, modelo=modeloC, placa=placaC, tamañoMotor=tamaño_motorC, propietarioT=propietarioC, conductorT=conductorC)
                change = True
                break
            i = i + 1
        
        if change == False:
            print("No se pueden ingresar más datos")

    # Buscar el propietario de algún taxi por medio de la cédula 
    def buscar_taxi_propietario():
        system('cls')
        if taxis[0] == 0:
            print("No se han ingresado datos aún")
        else:
            print("Ingresa la cédula del propietario abajo")
            cedula = int(input())

            let = False
            i = 0
            while i < len(taxis):
                if taxis[i]._propietarioT.cedula == cedula:
                    print(taxis[i].general_to_string())
                    let = True
                    break
                i = i + 1
            
            if let == False:
                print("Cédula no encontrada")
            

    # Calcular y mostrar el total a pagar con el salario de los conductores registrados
    def total_pagar_conductores():
        system('cls')
        if taxis[0] == 0:
            print("No se han ingresado datos aún")
        else:
            total_salario = 0
            i = 0
            while i < len(taxis):
                if taxis[i] != 0:
                    total_salario += taxis[i]._conductorT.salario
                else:
                    break # Because tha means that the index since this are empty
                i = i + 1
            
            print("El total a pagar es: " + str(total_salario))
                    
    # Mostar datos de un taxi en específico
    def datos_taxi():
        system('cls')
        if taxis[0] == 0:
            print("No se han ingresado datos aún")
        else:
            print("Ingrese la placa abajo")
            placa = str(input())
            let = False

            for i in taxis:
                if placa == i._placa:
                    print(i.taxi_to_string())
                    let = True
                    break
                elif i == 0:
                    break
            
            if let == False:
                print("Placa no encontrada.")

    # Mostrar el salario de un conductor en específico
    def salario_conductor():
        system('cls')
        if taxis[0] == 0:
            print("No se han ingresado datos aún")
        else:
            print("Ingrese la cédula del conductor abajo")
            cedula_conductor = int(input())

            pagar = 0
            i = 0
            let = False
            while i < len(taxis):
                if taxis[i]._conductorT.cedula == cedula_conductor:
                    pagar += taxis[i]._conductorT.salario
                    print("El salario para este conductor es: " + str(pagar))
                    let = True
                    break
                elif taxis[i] == 0:
                    break
                i = i + 1
            
            if let == False:
                print("Cédula no encontrada")


if __name__ == "__main__":
    system('cls')
    Cooperativa.__init__()


