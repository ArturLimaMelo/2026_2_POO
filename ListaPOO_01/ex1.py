import math
class Circulo:
    def __init__(self):
        self.raio = 0
    def area(self):
        return math.pi * self.raio ** 2
    def circunferencia(self):
        return 2 * math.pi * self.raio

x = Circulo()
x.raio = 5
y = Circulo()
y.raio = 3




