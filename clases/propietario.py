class Propietario:

    def __init__(self, cedula, nombre, telefono):
        self._cedula = cedula
        self._nombre = nombre
        self._telefono = telefono
    
    @property
    def cedula(self):
        return self.cedula

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
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono
    
    def toString(self):
        cadena = "Propietario{cedula : "+str(self._cedula)
        cadena += ", nombre : "+str(self._nombre)
        cadena += ", telefono : "+str(self._telefono)+"}"
        return cadena

if __name__ == '__main__':
    propietario = Propietario(cedula=10323020, nombre="Oracio", telefono= 3135063124)
    print(propietario.toString())