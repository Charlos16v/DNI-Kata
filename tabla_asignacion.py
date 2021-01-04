class TablaAsignacion:

    # Constructor de la tabla de asignación de letras validas para un DNI.
    def __init__(self):
        self.tablaLetras = [ 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E' ]


    # Getter encargado de obtener la letra de la tabla de asignación a partir de su posición, se encuentra dentro de una estructura try/catch para poder alcanzar posibles excepciones, principalmente la excepcion de que la letra se encuentre fuera del rango de alcance en la lista de letras.
    def getLetra(self, pos):
        try:
            return self.tablaLetras[pos]
        except:
            return "La posición de la letra se encuentra fuera del rango alcanzable."


    # Getter encargado de obtener la longitud de la tabla de asignación.
    def getTablaSize(self):
        return len(self.tablaLetras)

