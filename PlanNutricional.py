from Formulario import crear_interfaz_registros


class PlanNutricional:
    def __init__(self, **datos):
        self.id_plan_nutricional = datos.get("id_plan_nutricional", "")
        self.id_cliente = datos.get("id_cliente", "")
        self.id_nutricionista = datos.get("id_nutricionista", "")
        self.objetivo = datos.get("objetivo", "")
        self.calorias = datos.get("calorias", "")
        self.fecha_creacion = datos.get("fecha_creacion", "")
        self.alimentos = []

    def agregar_alimento(self, alimento):
        self.alimentos.append(alimento)

    def calcular_calorias(self):
        return sum(alimento.calcular_calorias(1) for alimento in self.alimentos)


def crear_interfaz(parent, planes):
    campos = [("id_plan_nutricional", "ID plan nutricional"), ("id_cliente", "ID cliente"),
              ("id_nutricionista", "ID nutricionista"), ("objetivo", "Objetivo"),
              ("calorias", "Calorías"), ("fecha_creacion", "Fecha de creación")]
    crear_interfaz_registros(parent, planes, PlanNutricional, campos, "Planes nutricionales")
