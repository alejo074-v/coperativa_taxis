class Propietario:

    def __init__(self, cedula, nombre, telefono):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
    
    @property
    def cedula(self):
        return self.cedula

    @cedula.setter
    def cedula(self, cedula):
        self.cedula = cedula
    
    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre
    
    @property
    def telefono(self):
        return self.telefono

    @telefono.setter
    def telefono(self, telefono):
        self.telefono = telefono
    
    def toString(self):
        return str(
            "Propietario{cedula=",self.cedula,
            ", nombre=",self.nombre,
            ", telefono=",self.telefono,
            "}"
        )

if __name__ == '__main__':
    propietario = Propietario(cedula=10323020, nombre="Oracio", telefono= 3135063124)
    print(propietario.toString())