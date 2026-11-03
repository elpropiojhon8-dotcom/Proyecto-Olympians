from Formulario import crear_interfaz_registros


class Ejercicio:
    def __init__(self, **datos):
        self.id_ejercicio = datos.get("id_ejercicio", "")
        self.nombre = datos.get("nombre", "")
        self.series = datos.get("series", "")
        self.repeticiones = datos.get("repeticiones", "")

    def modificar_series(self, series):
        self.series = int(series)

    def modificar_repeticiones(self, repeticiones):
        self.repeticiones = int(repeticiones)


def crear_interfaz(parent, ejercicios):
    campos = [("id_ejercicio", "ID ejercicio"), ("nombre", "Nombre"), ("series", "Series"), ("repeticiones", "Repeticiones")]
    crear_interfaz_registros(parent, ejercicios, Ejercicio, campos, "Registro de ejercicios")
