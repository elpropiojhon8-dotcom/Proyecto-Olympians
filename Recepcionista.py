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


def crear_interfaz(parent, recepcionistas):
    campos = [("id_recepcionista", "ID recepcionista"), ("nombres", "Nombres"), ("apellidos", "Apellidos"),
              ("telefono", "Teléfono"), ("turno", "Turno"), ("salario", "Salario")]
    crear_interfaz_registros(parent, recepcionistas, Recepcionista, campos, "Registro de recepcionistas")
