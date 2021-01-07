import tabla_asignacion

class Dni:

    # Constructor DNI, recogiendo la tabla de asignación de la clase TablaAsignacion.
    def __init__(self, cadena = ""):
        self.dni = cadena
        self.tabla = tabla_asignacion.TablaAsignacion()

    