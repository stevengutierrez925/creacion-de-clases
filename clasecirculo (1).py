import math

class circulo:
    def __init__(self, radio):
        self.radio = float(radio)

    def obtener_radio(self):
        return self.radio

    def establecer_radio(self, radio):
        self.radio = float(radio)

    def obtener_diametro(self):
        return self.radio * 2

    def establecer_diametro(self, diametro):
        self.radio = diametro / 2

    def area(self):
        return math.pi * self.radio ** 2

    def circunferencia(self):
        return 2 * math.pi * self.radio


if __name__ == "__main__":
    c1 = circulo(4)
    print("radio:", c1.obtener_radio())
    print("diametro:", c1.obtener_diametro())
    print("area:", c1.area())
    print("circunferencia:", c1.circunferencia())
