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



    def get_id_plan_nutricional(self):
        return self.id_plan_nutricional

    def set_id_plan_nutricional(self, valor):
        self.id_plan_nutricional = valor

    def get_id_cliente(self):
        return self.id_cliente

    def set_id_cliente(self, valor):
        self.id_cliente = valor

    def get_id_nutricionista(self):
        return self.id_nutricionista

    def set_id_nutricionista(self, valor):
        self.id_nutricionista = valor

    def get_objetivo(self):
        return self.objetivo

    def set_objetivo(self, valor):
        self.objetivo = valor

    def get_calorias(self):
        return self.calorias

    def set_calorias(self, valor):
        self.calorias = valor

    def get_fecha_creacion(self):
        return self.fecha_creacion

    def set_fecha_creacion(self, valor):
        self.fecha_creacion = valor

    def get_alimentos(self):
        return self.alimentos

    def set_alimentos(self, valor):
        self.alimentos = valor
def crear_interfaz(parent, planes):
    campos = [("id_plan_nutricional", "ID plan nutricional"), ("id_cliente", "ID cliente"),
              ("id_nutricionista", "ID nutricionista"), ("objetivo", "Objetivo"),
              ("calorias", "Calorías"), ("fecha_creacion", "Fecha de creación")]
    crear_interfaz_registros(parent, planes, PlanNutricional, campos, "Planes nutricionales")
