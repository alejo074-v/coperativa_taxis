class Conductor:

    def __init__(self, nombre, cedula, salario, contadorConductores):
        self._nombre = nombre
        self._cedula = cedula
        self._salario = salario
        self._contadorConductores = contadorConductores
    
    @property
    def nombre(self):
        return self.cedula
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def cedula(self):
        return self.cedula
    
    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula
    
    @property
    def salario(self):
        return self.salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario
    
    @property
    def contadorConductores(self):
        return self.contadorConductores
    
    @contadorConductores.setter
    def contadorConductores(self, contadorConductores):
        self._contadorConductores = contadorConductores

    def toString(self):
        cadena = "Conductor {nombre : " + str(self._nombre)
        cadena += ", cedula : " + str(self._cedula)
        cadena += ", salario : " + str(self._salario) + "}"
        return cadena

    def toString1(self):
        cadena = "Conductor [nombre : " + str(self._nombre)
        cadena += ", cedula : " + str(self._cedula)
        cadena += ", salario : " + str(self._salario) + "]"
        return cadena
        

if __name__ == "__main__":
    conductor = Conductor(nombre="Alejandro", cedula=1007213957, salario=1250000, contadorConductores=2)
    print(conductor.toString())