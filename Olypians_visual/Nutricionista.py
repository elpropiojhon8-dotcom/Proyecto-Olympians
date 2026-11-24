from Formulario import crear_interfaz_registros
from Persona import Persona


class Nutricionista(Persona):
    def __init__(self, **datos):
        super().__init__(**datos)
        self.id_nutricionista = datos.get("id_nutricionista", datos.get("id", ""))
        self.id = self.id_nutricionista
        self.especialidad = datos.get("especialidad", "")
        self.salario = datos.get("salario", "")
        self.planes = []

    def crear_plan(self, plan):
        self.planes.append(plan)

    def modificar_plan(self, indice, plan):
        if 0 <= indice < len(self.planes):
            self.planes[indice] = plan



    def get_id_nutricionista(self):
        return self.id_nutricionista

    def set_id_nutricionista(self, valor):
        self.id_nutricionista = valor

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

    def get_planes(self):
        return self.planes

    def set_planes(self, valor):
        self.planes = valor
def crear_interfaz(parent, nutricionistas):
    campos = [("id_nutricionista", "ID nutricionista"), ("nombres", "Nombres"), ("apellidos", "Apellidos"),
              ("telefono", "Teléfono"), ("especialidad", "Especialidad"), ("salario", "Salario")]
    crear_interfaz_registros(parent, nutricionistas, Nutricionista, campos, "Registro de nutricionistas")
