class Conductor:

    def __init__(self, cedula, nombre, salario):
        self._cedula = cedula
        self._nombre = nombre
        self._salario = salario

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    def toString(self):
        cadena = "Conductor{cedula="+str(self._cedula)
        cadena += ", nombre="+str(self._nombre)
        cadena += ", salario="+str(self._salario)+"}"
        return cadena

if __name__ == '__main__':
    conductor = Conductor(cedula=10323020, nombre="Oracio", salario= 800000)
    print(conductor.toString())
