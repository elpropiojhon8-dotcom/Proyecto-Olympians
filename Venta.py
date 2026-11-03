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


def crear_interfaz(parent, ventas):
    campos = [("id_venta", "ID venta"), ("id_producto", "ID producto"), ("id_cliente", "ID cliente"),
              ("fecha", "Fecha"), ("cantidad", "Cantidad"), ("total", "Total")]
    crear_interfaz_registros(parent, ventas, Venta, campos, "Registro de ventas")
