from Formulario import crear_interfaz_registros
from Persona import Persona


class Administrador(Persona):
    def __init__(self, **datos):
        super().__init__(**datos)
        self.id_administrador = datos.get("id_administrador", datos.get("id", ""))
        self.id = self.id_administrador
        self.usuario = datos.get("usuario", "")
        self.contrasena = datos.get("contrasena", "")
        self.clientes = []

    def gestionar_cliente(self, cliente):
        self.clientes.append(cliente)


def crear_interfaz(parent, administradores):
    campos = [("id_administrador", "ID administrador"), ("nombres", "Nombres"), ("apellidos", "Apellidos"),
              ("telefono", "Teléfono"), ("usuario", "Usuario"), ("contrasena", "Contraseña")]
    crear_interfaz_registros(parent, administradores, Administrador, campos, "Registro de administradores")
