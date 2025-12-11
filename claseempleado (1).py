class empleado:
    def __init__(self, nombre, edad, salario, cargo):
        self.nombre = nombre
        self.edad = int(edad)
        self.salario = float(salario)
        self.cargo = cargo

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = int(edad)

    def obtener_salario(self):
        return self.salario

    def establecer_salario(self, salario):
        self.salario = float(salario)

    def obtener_cargo(self):
        return self.cargo

    def establecer_cargo(self, cargo):
        self.cargo = cargo

    def salario_anual(self):
        return self.salario * 12


if __name__ == "__main__":
    emp = empleado("lucas", 30, 50000, "programador")
    print("salario anual:", emp.salario_anual())
