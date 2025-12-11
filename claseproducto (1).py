class producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def anadir_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, nombre_producto):
        for p in self.productos:
            if p.nombre == nombre_producto:
                self.productos.remove(p)
                return True
        return False

    def obtener_productos(self):
        return self.productos


if __name__ == "__main__":
    t = tienda("mi tienda")

    p1 = producto("camisa", 1500, 5)
    p2 = producto("pantalon", 2200, 3)

    t.anadir_producto(p1)
    t.anadir_producto(p2)

    print("productos actuales:", [p.nombre for p in t.obtener_productos()])
    t.eliminar_producto("camisa")
    print("despues de eliminar:", [p.nombre for p in t.obtener_productos()])
