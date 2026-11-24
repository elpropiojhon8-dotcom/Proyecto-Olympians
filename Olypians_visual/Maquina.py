from Formulario import crear_interfaz_registros


class Maquina:
    def __init__(self, **datos):
        self.id_maquina = datos.get("id_maquina", "")
        self.nombre = datos.get("nombre", "")
        self.tipo = datos.get("tipo", "")
        self.estado = datos.get("estado", "Disponible")

    def cambiar_estado(self, estado):
        self.estado = estado



    def get_id_maquina(self):
        return self.id_maquina

    def set_id_maquina(self, valor):
        self.id_maquina = valor

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, valor):
        self.nombre = valor

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, valor):
        self.tipo = valor

    def get_estado(self):
        return self.estado

    def set_estado(self, valor):
        self.estado = valor
def crear_interfaz(parent, maquinas):
    campos = [("id_maquina", "ID máquina"), ("nombre", "Nombre"), ("tipo", "Tipo"), ("estado", "Estado")]
    crear_interfaz_registros(parent, maquinas, Maquina, campos, "Registro de máquinas")
