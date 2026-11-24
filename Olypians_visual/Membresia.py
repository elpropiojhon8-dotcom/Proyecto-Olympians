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



    def get_id_membresia(self):
        return self.id_membresia

    def set_id_membresia(self, valor):
        self.id_membresia = valor

    def get_id_cliente(self):
        return self.id_cliente

    def set_id_cliente(self, valor):
        self.id_cliente = valor

    def get_id_plan(self):
        return self.id_plan

    def set_id_plan(self, valor):
        self.id_plan = valor

    def get_fecha_inicio(self):
        return self.fecha_inicio

    def set_fecha_inicio(self, valor):
        self.fecha_inicio = valor

    def get_fecha_fin(self):
        return self.fecha_fin

    def set_fecha_fin(self, valor):
        self.fecha_fin = valor

    def get_estado(self):
        return self.estado

    def set_estado(self, valor):
        self.estado = valor
def crear_interfaz(parent, membresias):
    campos = [("id_membresia", "ID membresía"), ("id_cliente", "ID cliente"), ("id_plan", "ID plan"),
              ("fecha_inicio", "Fecha de inicio"), ("fecha_fin", "Fecha de fin"), ("estado", "Estado")]
    crear_interfaz_registros(parent, membresias, Membresia, campos, "Registro de membresías")
