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


def crear_interfaz(parent, nutricionistas):
    campos = [("id_nutricionista", "ID nutricionista"), ("nombres", "Nombres"), ("apellidos", "Apellidos"),
              ("telefono", "Teléfono"), ("especialidad", "Especialidad"), ("salario", "Salario")]
    crear_interfaz_registros(parent, nutricionistas, Nutricionista, campos, "Registro de nutricionistas")
