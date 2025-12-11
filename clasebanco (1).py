import math

class banco:
    def __init__(self, nombre, tasa_interes_anual):
        self.nombre = nombre
        self.tasa = tasa_interes_anual / 100

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_tasa(self):
        return self.tasa * 100

    def establecer_tasa(self, tasa):
        self.tasa = tasa / 100

    def calcular_interes(self, cantidad, años):
        return cantidad * (1 + self.tasa) ** años

    def tiempo_para_duplicar(self):
        return math.log(2) / math.log(1 + self.tasa)


if __name__ == "__main__":
    b1 = banco("banco nacion", 5)
    print("monto tras 3 años:", b1.calcular_interes(10000, 3))
    print("años para duplicar:", round(b1.tiempo_para_duplicar(), 2))
