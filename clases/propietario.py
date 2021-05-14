class Propietario:

    def __init__(self, nombre, cedula, telefono):
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono


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
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    def toString(self):
        cadena = "Propietario{cedula="+str(self._cedula)
        cadena += ", nombre="+str(self._nombre)
        cadena += ", telefono="+str(self._telefono)+"}"
        return cadena
