from Formulario import crear_interfaz_registros


class Mantenimiento:
    def __init__(self, **datos):
        self.id_mantenimiento = datos.get("id_mantenimiento", "")
        self.id_maquina = datos.get("id_maquina", "")
        self.fecha = datos.get("fecha", "")
        self.descripcion = datos.get("descripcion", "")
        self.costo = datos.get("costo", "")

    def calcular_costo(self):
        return float(self.costo or 0)


def crear_interfaz(parent, mantenimientos):
    campos = [("id_mantenimiento", "ID mantenimiento"), ("id_maquina", "ID máquina"),
              ("fecha", "Fecha"), ("descripcion", "Descripción"), ("costo", "Costo")]
    crear_interfaz_registros(parent, mantenimientos, Mantenimiento, campos, "Registro de mantenimientos")
