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



    def get_id_rutina(self):
        return self.id_rutina

    def set_id_rutina(self, valor):
        self.id_rutina = valor

    def get_id_cliente(self):
        return self.id_cliente

    def set_id_cliente(self, valor):
        self.id_cliente = valor

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, valor):
        self.nombre = valor

    def get_nivel(self):
        return self.nivel

    def set_nivel(self, valor):
        self.nivel = valor

    def get_objetivo(self):
        return self.objetivo

    def set_objetivo(self, valor):
        self.objetivo = valor

    def get_ejercicios(self):
        return self.ejercicios

    def set_ejercicios(self, valor):
        self.ejercicios = valor
def crear_interfaz(parent, rutinas):
    campos = [("id_rutina", "ID rutina"), ("id_cliente", "ID cliente"), ("nombre", "Nombre"),
              ("nivel", "Nivel"), ("objetivo", "Objetivo")]
    crear_interfaz_registros(parent, rutinas, Rutina, campos, "Registro de rutinas")
