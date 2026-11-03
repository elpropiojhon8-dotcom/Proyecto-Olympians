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


def crear_interfaz(parent, planes):
    campos = [("id_plan", "ID plan"), ("nombre", "Nombre"), ("precio", "Precio"), ("duracion", "Duración (días)")]
    crear_interfaz_registros(parent, planes, Plan, campos, "Planes de membresía")
