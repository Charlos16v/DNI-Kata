from src.tabla_asignacion import *

class Dni:

    # Constructor DNI, recogiendo la tabla de asignación de la clase TablaAsignacion.
    def __init__(self, cadena = ""):
        self.dni = cadena
        self.tabla = TablaAsignacion()

    # Metodo encargado de construir un numero de DNI valido a partir de un numero que cumpla con las condiciones de longitud establecidas en las constantes de la clase TablaAsignacion.
    def buildDni(number):
        if len(number) == TablaAsignacion.DNI_NUMBER_PART_LENGHT:
            DNI = str(number)+ TablaAsignacion.getLetra(number)
            if len(DNI) == TablaAsignacion.DNI_TOTAL_LENGTH:
                return DNI
        else:
            print("El numero de DNI es incorrecto")
