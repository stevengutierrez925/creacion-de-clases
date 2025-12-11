from datetime import datetime

class coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def obtener_marca(self):
        return self.marca

    def establecer_marca(self, marca):
        self.marca = marca

    def obtener_modelo(self):
        return self.modelo

    def establecer_modelo(self, modelo):
        self.modelo = modelo

    def obtener_año(self):
        return self.año

    def establecer_año(self, año):
        self.año = año

    def años_desde_fabricacion(self):
        año_actual = datetime.now().year
        return año_actual - int(self.año)


if __name__ == "__main__":
    coche1 = coche("ferrari", "Ferrari 275", 2015)
    print("marca:", coche1.obtener_marca())
    print("modelo:", coche1.obtener_modelo())
    print("año:", coche1.obtener_año())
    print("años desde fabricacion:", coche1.años_desde_fabricacion())

