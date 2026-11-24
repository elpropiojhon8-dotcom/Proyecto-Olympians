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



    def get_id_asistencia(self):
        return self.id_asistencia

    def set_id_asistencia(self, valor):
        self.id_asistencia = valor

    def get_id_cliente(self):
        return self.id_cliente

    def set_id_cliente(self, valor):
        self.id_cliente = valor

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, valor):
        self.fecha = valor

    def get_hora_entrada(self):
        return self.hora_entrada

    def set_hora_entrada(self, valor):
        self.hora_entrada = valor

    def get_hora_salida(self):
        return self.hora_salida

    def set_hora_salida(self, valor):
        self.hora_salida = valor
def crear_interfaz(parent, asistencias):
    campos = [("id_asistencia", "ID asistencia"), ("id_cliente", "ID cliente"), ("fecha", "Fecha"),
              ("hora_entrada", "Hora de entrada"), ("hora_salida", "Hora de salida")]
    crear_interfaz_registros(parent, asistencias, Asistencia, campos, "Registro de asistencias")
