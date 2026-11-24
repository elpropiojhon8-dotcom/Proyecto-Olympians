from Formulario import crear_interfaz_registros


class Plan:
    def __init__(self, **datos):
        self.id_plan = datos.get("id_plan", "")
        self.nombre = datos.get("nombre", "")
        self.precio = datos.get("precio", "")
        self.duracion = datos.get("duracion", "")

    def calcular_precio(self):
        return float(self.precio or 0)

    def cambiar_precio(self, precio):
        self.precio = float(precio)



    def get_id_plan(self):
        return self.id_plan

    def set_id_plan(self, valor):
        self.id_plan = valor

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, valor):
        self.nombre = valor

    def get_precio(self):
        return self.precio

    def set_precio(self, valor):
        self.precio = valor

    def get_duracion(self):
        return self.duracion

    def set_duracion(self, valor):
        self.duracion = valor
def crear_interfaz(parent, planes):
    campos = [("id_plan", "ID plan"), ("nombre", "Nombre"), ("precio", "Precio"), ("duracion", "Duración (días)")]
    crear_interfaz_registros(parent, planes, Plan, campos, "Planes de membresía")
