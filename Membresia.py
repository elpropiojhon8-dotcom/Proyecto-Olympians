from Formulario import crear_interfaz_registros


class Membresia:
    def __init__(self, **datos):
        self.id_membresia = datos.get("id_membresia", "")
        self.id_cliente = datos.get("id_cliente", "")
        self.id_plan = datos.get("id_plan", "")
        self.fecha_inicio = datos.get("fecha_inicio", "")
        self.fecha_fin = datos.get("fecha_fin", "")
        self.estado = datos.get("estado", "Activa")

    def activar(self):
        self.estado = "Activa"

    def renovar(self, fecha_fin):
        self.fecha_fin = fecha_fin
        self.estado = "Activa"

    def verificar_estado(self):
        return self.estado


def crear_interfaz(parent, membresias):
    campos = [("id_membresia", "ID membresía"), ("id_cliente", "ID cliente"), ("id_plan", "ID plan"),
              ("fecha_inicio", "Fecha de inicio"), ("fecha_fin", "Fecha de fin"), ("estado", "Estado")]
    crear_interfaz_registros(parent, membresias, Membresia, campos, "Registro de membresías")
