from Formulario import crear_interfaz_registros


class Producto:
    def __init__(self, **datos):
        self.id_producto = datos.get("id_producto", "")
        self.nombre = datos.get("nombre", "")
        self.precio = datos.get("precio", "")
        self.stock = datos.get("stock", "")

    def vender(self, cantidad):
        cantidad = int(cantidad)
        if cantidad <= int(self.stock or 0):
            self.stock = int(self.stock or 0) - cantidad
            return True
        return False

    def actualizar_stock(self, cantidad):
        self.stock = int(cantidad)


def crear_interfaz(parent, productos):
    campos = [("id_producto", "ID producto"), ("nombre", "Nombre"), ("precio", "Precio"), ("stock", "Stock")]
    crear_interfaz_registros(parent, productos, Producto, campos, "Registro de productos")
