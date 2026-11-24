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



    def get_id_producto(self):
        return self.id_producto

    def set_id_producto(self, valor):
        self.id_producto = valor

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, valor):
        self.nombre = valor

    def get_precio(self):
        return self.precio

    def set_precio(self, valor):
        self.precio = valor

    def get_stock(self):
        return self.stock

    def set_stock(self, valor):
        self.stock = valor
def crear_interfaz(parent, productos):
    campos = [("id_producto", "ID producto"), ("nombre", "Nombre"), ("precio", "Precio"), ("stock", "Stock")]
    crear_interfaz_registros(parent, productos, Producto, campos, "Registro de productos")
