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



    def get_id_entrenador(self):
        return self.id_entrenador

    def set_id_entrenador(self, valor):
        self.id_entrenador = valor

    def get_id(self):
        return self.id

    def set_id(self, valor):
        self.id = valor

    def get_especialidad(self):
        return self.especialidad

    def set_especialidad(self, valor):
        self.especialidad = valor

    def get_salario(self):
        return self.salario

    def set_salario(self, valor):
        self.salario = valor

    def get_clientes(self):
        return self.clientes

    def set_clientes(self, valor):
        self.clientes = valor
def crear_interfaz(parent, entrenadores):
    campos = [("id_entrenador", "ID entrenador"), ("nombres", "Nombres"), ("apellidos", "Apellidos"),
              ("telefono", "Teléfono"), ("especialidad", "Especialidad"), ("salario", "Salario")]
    crear_interfaz_registros(parent, entrenadores, Entrenador, campos, "Registro de entrenadores")
