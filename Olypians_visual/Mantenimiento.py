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



    def get_id_mantenimiento(self):
        return self.id_mantenimiento

    def set_id_mantenimiento(self, valor):
        self.id_mantenimiento = valor

    def get_id_maquina(self):
        return self.id_maquina

    def set_id_maquina(self, valor):
        self.id_maquina = valor

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, valor):
        self.fecha = valor

    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, valor):
        self.descripcion = valor

    def get_costo(self):
        return self.costo

    def set_costo(self, valor):
        self.costo = valor
def crear_interfaz(parent, mantenimientos):
    campos = [("id_mantenimiento", "ID mantenimiento"), ("id_maquina", "ID máquina"),
              ("fecha", "Fecha"), ("descripcion", "Descripción"), ("costo", "Costo")]
    crear_interfaz_registros(parent, mantenimientos, Mantenimiento, campos, "Registro de mantenimientos")
