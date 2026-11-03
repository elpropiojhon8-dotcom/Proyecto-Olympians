from Formulario import crear_interfaz_registros


class Rutina:
    def __init__(self, **datos):
        self.id_rutina = datos.get("id_rutina", "")
        self.id_cliente = datos.get("id_cliente", "")
        self.nombre = datos.get("nombre", "")
        self.nivel = datos.get("nivel", "")
        self.objetivo = datos.get("objetivo", "")
        self.ejercicios = []

    def agregar_ejercicio(self, ejercicio):
        self.ejercicios.append(ejercicio)

    def eliminar_ejercicio(self, ejercicio):
        if ejercicio in self.ejercicios:
            self.ejercicios.remove(ejercicio)


def crear_interfaz(parent, rutinas):
    campos = [("id_rutina", "ID rutina"), ("id_cliente", "ID cliente"), ("nombre", "Nombre"),
              ("nivel", "Nivel"), ("objetivo", "Objetivo")]
    crear_interfaz_registros(parent, rutinas, Rutina, campos, "Registro de rutinas")
