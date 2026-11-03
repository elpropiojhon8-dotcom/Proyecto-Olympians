from Formulario import crear_interfaz_registros


class Asistencia:
    def __init__(self, **datos):
        self.id_asistencia = datos.get("id_asistencia", "")
        self.id_cliente = datos.get("id_cliente", "")
        self.fecha = datos.get("fecha", "")
        self.hora_entrada = datos.get("hora_entrada", "")
        self.hora_salida = datos.get("hora_salida", "")

    def registrar_entrada(self, hora):
        self.hora_entrada = hora

    def registrar_salida(self, hora):
        self.hora_salida = hora


def crear_interfaz(parent, asistencias):
    campos = [("id_asistencia", "ID asistencia"), ("id_cliente", "ID cliente"), ("fecha", "Fecha"),
              ("hora_entrada", "Hora de entrada"), ("hora_salida", "Hora de salida")]
    crear_interfaz_registros(parent, asistencias, Asistencia, campos, "Registro de asistencias")
