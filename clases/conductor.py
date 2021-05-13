class Conductor:

    def __init__(self, nombre, cedula, salario): #contadorConductores):
        self._nombre = nombre
        self._cedula = cedula
        self._salario = salario
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def cedula(self):
        return self._cedula
    
    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario
