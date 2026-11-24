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



    def get_id_administrador(self):
        return self.id_administrador

    def set_id_administrador(self, valor):
        self.id_administrador = valor

    def get_id(self):
        return self.id

    def set_id(self, valor):
        self.id = valor

    def get_usuario(self):
        return self.usuario

    def set_usuario(self, valor):
        self.usuario = valor

    def get_contrasena(self):
        return self.contrasena

    def set_contrasena(self, valor):
        self.contrasena = valor

    def get_clientes(self):
        return self.clientes

    def set_clientes(self, valor):
        self.clientes = valor
def crear_interfaz(parent, administradores):
    campos = [("id_administrador", "ID administrador"), ("nombres", "Nombres"), ("apellidos", "Apellidos"),
              ("telefono", "Teléfono"), ("usuario", "Usuario"), ("contrasena", "Contraseña")]
    crear_interfaz_registros(parent, administradores, Administrador, campos, "Registro de administradores")
