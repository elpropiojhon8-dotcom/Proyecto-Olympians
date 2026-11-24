from Formulario import crear_interfaz_registros
from Persona import Persona


class Recepcionista(Persona):
    def __init__(self, **datos):
        super().__init__(**datos)
        self.id_recepcionista = datos.get("id_recepcionista", datos.get("id", ""))
        self.id = self.id_recepcionista
        self.turno = datos.get("turno", "")
        self.salario = datos.get("salario", "")
        self.clientes = []

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)



    def get_id_recepcionista(self):
        return self.id_recepcionista

    def set_id_recepcionista(self, valor):
        self.id_recepcionista = valor

    def get_id(self):
        return self.id

    def set_id(self, valor):
        self.id = valor

    def get_turno(self):
        return self.turno

    def set_turno(self, valor):
        self.turno = valor

    def get_salario(self):
        return self.salario

    def set_salario(self, valor):
        self.salario = valor

    def get_clientes(self):
        return self.clientes

    def set_clientes(self, valor):
        self.clientes = valor
def crear_interfaz(parent, recepcionistas):
    campos = [("id_recepcionista", "ID recepcionista"), ("nombres", "Nombres"), ("apellidos", "Apellidos"),
              ("telefono", "Teléfono"), ("turno", "Turno"), ("salario", "Salario")]
    crear_interfaz_registros(parent, recepcionistas, Recepcionista, campos, "Registro de recepcionistas")
