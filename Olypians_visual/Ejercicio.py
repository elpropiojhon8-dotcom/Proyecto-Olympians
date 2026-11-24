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



    def get_id_ejercicio(self):
        return self.id_ejercicio

    def set_id_ejercicio(self, valor):
        self.id_ejercicio = valor

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, valor):
        self.nombre = valor

    def get_series(self):
        return self.series

    def set_series(self, valor):
        self.series = valor

    def get_repeticiones(self):
        return self.repeticiones

    def set_repeticiones(self, valor):
        self.repeticiones = valor
def crear_interfaz(parent, ejercicios):
    campos = [("id_ejercicio", "ID ejercicio"), ("nombre", "Nombre"), ("series", "Series"), ("repeticiones", "Repeticiones")]
    crear_interfaz_registros(parent, ejercicios, Ejercicio, campos, "Registro de ejercicios")
