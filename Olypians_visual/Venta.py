from Formulario import crear_interfaz_registros


class Venta:
    def __init__(self, **datos):
        self.id_venta = datos.get("id_venta", "")
        self.id_producto = datos.get("id_producto", "")
        self.id_cliente = datos.get("id_cliente", "")
        self.fecha = datos.get("fecha", "")
        self.cantidad = datos.get("cantidad", "")
        self.total = datos.get("total", "")

    def agregar_producto(self, producto, cantidad):
        if producto.vender(cantidad):
            self.id_producto = producto.id_producto
            self.cantidad = int(cantidad)
            self.total = float(producto.precio) * int(cantidad)
            return True
        return False

    def calcular_total(self):
        return float(self.total or 0)



    def get_id_venta(self):
        return self.id_venta

    def set_id_venta(self, valor):
        self.id_venta = valor

    def get_id_producto(self):
        return self.id_producto

    def set_id_producto(self, valor):
        self.id_producto = valor

    def get_id_cliente(self):
        return self.id_cliente

    def set_id_cliente(self, valor):
        self.id_cliente = valor

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, valor):
        self.fecha = valor

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, valor):
        self.cantidad = valor

    def get_total(self):
        return self.total

    def set_total(self, valor):
        self.total = valor
def crear_interfaz(parent, ventas):
    campos = [("id_venta", "ID venta"), ("id_producto", "ID producto"), ("id_cliente", "ID cliente"),
              ("fecha", "Fecha"), ("cantidad", "Cantidad"), ("total", "Total")]
    crear_interfaz_registros(parent, ventas, Venta, campos, "Registro de ventas")
