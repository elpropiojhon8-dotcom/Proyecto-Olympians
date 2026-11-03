from Formulario import crear_interfaz_registros


class Maquina:
    def __init__(self, **datos):
        self.id_maquina = datos.get("id_maquina", "")
        self.nombre = datos.get("nombre", "")
        self.tipo = datos.get("tipo", "")
        self.estado = datos.get("estado", "Disponible")

    def cambiar_estado(self, estado):
        self.estado = estado


def crear_interfaz(parent, maquinas):
    campos = [("id_maquina", "ID máquina"), ("nombre", "Nombre"), ("tipo", "Tipo"), ("estado", "Estado")]
    crear_interfaz_registros(parent, maquinas, Maquina, campos, "Registro de máquinas")
