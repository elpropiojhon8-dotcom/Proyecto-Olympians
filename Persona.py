from Formulario import crear_interfaz_registros


class Persona:
    def __init__(self, **datos):
        self.id = datos.get("id", "")
        self.nombres = datos.get("nombres", "")
        self.apellidos = datos.get("apellidos", "")
        self.telefono = datos.get("telefono", "")


def crear_interfaz(parent, personas):
    campos = [("id", "ID"), ("nombres", "Nombres"), ("apellidos", "Apellidos"), ("telefono", "Teléfono")]
    crear_interfaz_registros(parent, personas, Persona, campos, "Personas")
