from Formulario import crear_interfaz_registros
from Persona import Persona


class Entrenador(Persona):
    def __init__(self, **datos):
        super().__init__(**datos)
        self.id_entrenador = datos.get("id_entrenador", datos.get("id", ""))
        self.id = self.id_entrenador
        self.especialidad = datos.get("especialidad", "")
        self.salario = datos.get("salario", "")
        self.clientes = []

    def asignar_cliente(self, cliente):
        if cliente not in self.clientes:
            self.clientes.append(cliente)


def crear_interfaz(parent, entrenadores):
    campos = [("id_entrenador", "ID entrenador"), ("nombres", "Nombres"), ("apellidos", "Apellidos"),
              ("telefono", "Teléfono"), ("especialidad", "Especialidad"), ("salario", "Salario")]
    crear_interfaz_registros(parent, entrenadores, Entrenador, campos, "Registro de entrenadores")
