class producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = float(precio)

    def obtener_stock(self):
        return self.stock

    def establecer_stock(self, stock):
        self.stock = int(stock)

    def aumentar_stock(self, cantidad):
        self.stock += int(cantidad)

    def disminuir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= int(cantidad)
        else:
            print("no hay suficiente stock para disminuir")


if __name__ == "__main__":
    p1 = producto("camisa", 1500, 10)
    print("stock inicial:", p1.obtener_stock())
    p1.aumentar_stock(5)
    print("stock despues de aumentar:", p1.obtener_stock())
    p1.disminuir_stock(8)
    print("stock final:", p1.obtener_stock())
