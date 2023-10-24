from Empleado import*

class Operario(Empleado):
    def __str__(self):
        return super().__str__() + "-> " + "Operario"