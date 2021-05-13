import conductor, propietario

class Taxi:

    def __init__(self, marca, modelo, placa, tamMotor, propietariot, conductort):
        self._marca = marca
        self._modelo = modelo
        self._placa = placa
        self._tamMotor = tamMotor
        self._propietariot = propietariot
        self._conductort = conductort

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

    @property
    def propietario(self):
        return self._propietariot
    @propietario.setter
    def propietario(self, propietario):
        self._propietariot = propietario

    @property
    def conductor(self):
        return self._conductort
    @conductor.setter
    def conductor(self, conductor):
        self._conductort = conductor

    def toString(self):
        cadena = "Taxi{marca="+str(self._marca)
        cadena += ", modelo="+str(self._modelo)
        cadena += ", placa="+str(self._placa)
        cadena += ", tamañoMotor="+str(self._tamMotor)
        cadena += ", propietario="+self._propietariot.toString()
        cadena += ", conductor="+self._conductort.toString()+"}"
        return cadena

if __name__ == '__main__':
    propietario1 = propietario.Propietario(cedula=10323020, nombre="Daniel", telefono= 3135063124)
    conductor1 = conductor.Conductor(cedula=10323020, nombre="Oracio", salario= 800000)
    taxi = Taxi(marca = "audi", modelo = 2018, placa="ACB112", tamMotor= 1500, propietariot = propietario1, conductort = conductor1)
    print(taxi.propietario.cedula)
