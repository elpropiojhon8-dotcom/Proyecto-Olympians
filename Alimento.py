from Formulario import crear_interfaz_registros


class Alimento:
    def __init__(self, **datos):
        self.id_alimento = datos.get("id_alimento", "")
        self.nombre = datos.get("nombre", "")
        self.calorias = datos.get("calorias", "")
        self.proteinas = datos.get("proteinas", "")

    def calcular_calorias(self, cantidad):
        return float(self.calorias or 0) * float(cantidad)


def crear_interfaz(parent, alimentos):
    campos = [("id_alimento", "ID alimento"), ("nombre", "Nombre"),
              ("calorias", "Calorías"), ("proteinas", "Proteínas")]
    crear_interfaz_registros(parent, alimentos, Alimento, campos, "Registro de alimentos")
