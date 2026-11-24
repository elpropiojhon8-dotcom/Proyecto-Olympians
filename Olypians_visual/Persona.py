from Formulario import crear_interfaz_registros


class Persona:
    def __init__(self, **datos):
        self.id = datos.get("id", "")
        self.nombres = datos.get("nombres", "")
        self.apellidos = datos.get("apellidos", "")
        self.telefono = datos.get("telefono", "")



    def get_id(self):
        return self.id

    def set_id(self, valor):
        self.id = valor

    def get_nombres(self):
        return self.nombres

    def set_nombres(self, valor):
        self.nombres = valor

    def get_apellidos(self):
        return self.apellidos

    def set_apellidos(self, valor):
        self.apellidos = valor

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, valor):
        self.telefono = valor
def crear_interfaz(parent, personas):
    campos = [("id", "ID"), ("nombres", "Nombres"), ("apellidos", "Apellidos"), ("telefono", "Teléfono")]
    crear_interfaz_registros(parent, personas, Persona, campos, "Personas")
