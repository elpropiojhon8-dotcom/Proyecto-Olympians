from Formulario import crear_interfaz_registros


class Horario:
    def __init__(self, **datos):
        self.id_horario = datos.get("id_horario", "")
        self.dia = datos.get("dia", "")
        self.hora_inicio = datos.get("hora_inicio", "")
        self.hora_fin = datos.get("hora_fin", "")

    def modificar_horario(self, hora_inicio, hora_fin):
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin


def crear_interfaz(parent, horarios):
    campos = [("id_horario", "ID horario"), ("dia", "Día"), ("hora_inicio", "Hora de inicio"), ("hora_fin", "Hora de fin")]
    crear_interfaz_registros(parent, horarios, Horario, campos, "Registro de horarios")
