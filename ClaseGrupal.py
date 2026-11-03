from Formulario import crear_interfaz_registros


class ClaseGrupal:
    def __init__(self, **datos):
        self.id_clase = datos.get("id_clase", "")
        self.nombre = datos.get("nombre", "")
        self.capacidad = datos.get("capacidad", "")
        self.id_horario = datos.get("id_horario", "")
        self.clientes = []

    def agregar_cliente(self, cliente):
        if len(self.clientes) < int(self.capacidad or 0):
            self.clientes.append(cliente)
            return True
        return False

    def eliminar_cliente(self, cliente):
        if cliente in self.clientes:
            self.clientes.remove(cliente)

    def consultar_cupos(self):
        return max(0, int(self.capacidad or 0) - len(self.clientes))


def crear_interfaz(parent, clases):
    campos = [("id_clase", "ID clase"), ("nombre", "Nombre"), ("capacidad", "Capacidad"), ("id_horario", "ID horario")]
    crear_interfaz_registros(parent, clases, ClaseGrupal, campos, "Registro de clases grupales")
