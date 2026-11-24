from Formulario import crear_interfaz_registros


class Pago:
    def __init__(self, **datos):
        self.id_pago = datos.get("id_pago", "")
        self.id_cliente = datos.get("id_cliente", "")
        self.fecha = datos.get("fecha", "")
        self.valor = datos.get("valor", "")
        self.metodo = datos.get("metodo", "")

    def realizar_pago(self, valor):
        self.valor = float(valor)
        return True

    def generar_comprobante(self):
        return f"Comprobante {self.id_pago} | Cliente {self.id_cliente} | Valor {self.valor}"



    def get_id_pago(self):
        return self.id_pago

    def set_id_pago(self, valor):
        self.id_pago = valor

    def get_id_cliente(self):
        return self.id_cliente

    def set_id_cliente(self, valor):
        self.id_cliente = valor

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, valor):
        self.fecha = valor

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def get_metodo(self):
        return self.metodo

    def set_metodo(self, valor):
        self.metodo = valor
def crear_interfaz(parent, pagos):
    campos = [("id_pago", "ID pago"), ("id_cliente", "ID cliente"), ("fecha", "Fecha"),
              ("valor", "Valor"), ("metodo", "Método")]
    crear_interfaz_registros(parent, pagos, Pago, campos, "Registro de pagos")
