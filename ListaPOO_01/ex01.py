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
z = x        # é feito aqui uma cópia da referência
z.raio = 20

print(x, x.raio, x.area(), x.circunferencia())
print(y, y.raio, y.area(), y.circunferencia())


        