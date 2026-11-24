from Formulario import crear_interfaz_registros


class Alimento:
    def __init__(self, **datos):
        self.id_alimento = datos.get("id_alimento", "")
        self.nombre = datos.get("nombre", "")
        self.calorias = datos.get("calorias", "")
        self.proteinas = datos.get("proteinas", "")

    def calcular_calorias(self, cantidad):
        return float(self.calorias or 0) * float(cantidad)



    def get_id_alimento(self):
        return self.id_alimento

    def set_id_alimento(self, valor):
        self.id_alimento = valor

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, valor):
        self.nombre = valor

    def get_calorias(self):
        return self.calorias

    def set_calorias(self, valor):
        self.calorias = valor

    def get_proteinas(self):
        return self.proteinas

    def set_proteinas(self, valor):
        self.proteinas = valor
def crear_interfaz(parent, alimentos):
    campos = [("id_alimento", "ID alimento"), ("nombre", "Nombre"),
              ("calorias", "Calorías"), ("proteinas", "Proteínas")]
    crear_interfaz_registros(parent, alimentos, Alimento, campos, "Registro de alimentos")
