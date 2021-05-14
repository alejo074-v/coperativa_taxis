from propietario import Propietario
from conductor import Conductor

class Taxi:
    def __init__(self, marca, modelo, placa, tamMotor, propietarioT, conductorT):
        self._marca = marca
        self._modelo = modelo
        self._placa = placa
        self._tamMotor = tamMotor
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
    def tamMotor(self):
        return self._tamMotor

    @tamMotor.setter
    def tamMotor(self, tamMotor):
        self._tamMotor = tamMotor


    def toString(self):
        cadena = "Taxi{marca="+str(self._marca)
        cadena += ", modelo="+str(self._modelo)
        cadena += ", placa="+str(self._placa)
        cadena += ", tamañoMotor="+str(self._tamMotor)
        cadena += ", propietario="+self._propietarioT.toString()
        cadena += ", conductor="+self._conductorT.toString()+"}"
        return cadena

    def taxi_to_string(self):
        cadena = "Marca : " + str(self._marca)
        cadena += ", modelo : " + str(self.modelo)
        cadena += ", placa : " + str(self.placa)
        cadena += ", tama\u00f1oMotor : " + str(self.tamMotor)
        return cadena
