import conductor, propietario
class Taxi:
    def __init__(self, marca, modelo, placa, tamañoMotor, propietarioT, conductorT):
        self._marca = marca
        self._modelo = modelo
        self._placa = placa
        self._tamañoMotor = tamañoMotor
        self._propietarioT = propietarioT
        self._conductorT = conductorT

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def placa(self):
        return self._placa
    
    @placa.setter
    def placa(self, placa):
        self._placa = placa

    @property
    def tamañoMotor(self):
        return self._tamañoMotor
    
    @tamañoMotor.setter
    def tamañoMotor(self, tamañoMotor):
        self._tamañoMotor = tamañoMotor


    def toString(self):
        cadena = "Taxi{marca : " + str(self._marca)
        cadena += ", modelo : " + str(self.modelo)
        cadena += ", placa : " + str(self.placa)
        cadena += ", tama\u00f1oMotor : " + str(self.tamañoMotor)
        cadena += ", " + self._propietarioT.toString1()
        cadena += ", " + self._conductorT.toString1() + "}"
        return cadena

if __name__ == "__main__":
    propietario = propietario.Propietario(cedula=10323020, nombre="Oracio", telefono= 3135063124)
    conductor = conductor.Conductor(nombre="Alejandro", cedula=1007213957, salario=1250000, contadorConductores=2)
    taxi = Taxi(marca="Cars", modelo=2014, placa="UTF-8", tamañoMotor=3000, propietarioT = propietario, conductorT = conductor)
    print(taxi.toString())