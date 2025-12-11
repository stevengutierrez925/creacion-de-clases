class estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = int(edad)
        self.carrera = carrera

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = int(edad)

    def obtener_carrera(self):
        return self.carrera

    def establecer_carrera(self, carrera):
        self.carrera = carrera

    def nota_media(self, notas):
        if len(notas) == 0:
            return None
        return sum(notas) / len(notas)


if __name__ == "__main__":
    e1 = estudiante("maria", 20, "informatica")
    print("nombre:", e1.obtener_nombre())
    print("nota media:", e1.nota_media([7, 8, 9, 10]))
