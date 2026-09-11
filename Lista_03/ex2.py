class Frete:
    def __init__(self, distancia : float, peso : float):
        self.distancia = distancia
        self.peso = peso

    def Frete(self, distancia : float, peso : float):
        if (distancia <= 0 or peso <= 0):
            print("Valores devem ser positivos")
        else:
            self.distancia = distancia
            self.peso = peso

    def setDistancia(self, d : float):
        self.distancia = d
    
    def getDistancia(self):
        return self.distancia

    def setPeso(self, p : float):
        self.peso = p

    def getPeso(self):
        return self.peso

    def calcFrete(self):
        return self.peso * self.distancia * 0.01

    def ToString(self):
        return f"O frete tem peso {self.peso}Kg e percorre {self.distancia}Km" 