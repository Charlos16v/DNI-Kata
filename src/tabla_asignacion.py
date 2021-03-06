class TablaAsignacion:

    # Constructor de la tabla de asignación de letras validas para un DNI.
    def __init__(self):
        self.tablaLetras = [ 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E' ]


    DNI_TOTAL_LENGTH = 9
    DNI_NUMBER_PART_LENGHT = DNI_TOTAL_LENGTH-1

    # Getter encargado de obtener la letra de la tabla de asignación a partir de su posición, se encuentra dentro de una estructura try/catch para poder alcanzar posibles excepciones, principalmente la excepcion de que la letra se encuentre fuera del rango de alcance en la lista de letras.
    def getLetra(self, pos):
        try:
            return self.tablaLetras[pos]
        except:
            return "La posición de la letra se encuentra fuera del rango alcanzable."


    # Getter encargado de obtener la longitud de la tabla de asignación.
    def getTablaSize(self):
        return len(self.tablaLetras)


    # Getter encargado de obtener la letra únicamente si se encuentra en la tabla de asignación de letras.
    def getLetraCorrecta(self, letra):
        return letra in self.tablaLetras

    # Metodo encargado de calcular la letra asignada a partir del resto obtenido en la division del numero por el tamaño de la lista de letras (23).
    def calcularLetra(self, DNI):
        pos = int(DNI) % self.getTablaSize()
        return self.getLetra(pos)
