import math

class retangulo:
    def __init__(self, b : float, h : float):
        self.b = b
        self.h = h
    def Retangulo(self, b : float, h : float):
        if (b > 0 and h > 0):
            self.b = b
            self.h = h
        else: raise ValueError("As medidas devem ser positivas")

    def setBase(self, b : float):
        self.__b = b
    
    def setAltura(self, h : float):
        self.__h = h

    def getAltura(self):
        return self.__h

    def getBase(self):
        return self.__b

    def calcArea(self):
        return self.__b * self.__h

    def calcDiagonal(self):
        return math.sqrt(self.__b ** 2 + self.__h ** 2)

    def ToString(self):
        return f"O retângulo tem base {self.__b} e altura {self.__h}"


