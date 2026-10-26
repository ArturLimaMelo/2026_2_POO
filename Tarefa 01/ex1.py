class Viagem:
    def __init__(self, destino : str, distancia : float, litros : float):
        if (distancia < 0 or litros <= 0):
            print("Valores devem ser positivos")
        else:
            self.destino = destino
            self.distancia = distancia
            self.litros = litros

    def Viagem(self, destino : str, distancia : float, litros : float):
            self.destino = destino
            self.distancia = distancia
            self.litros = litros

    def Consumo(self):
        return self.distancia / self.litros

    def ToString(self):
        return f"Viagem para {self.destino} com distância de {self.distancia}Kms com {self.litros} litros de combustível"

    def getDestino(self):
        return self.destino

    def setDestino(self, d : str):
        self.destino = d

    def getDistancia(self):
        return self.distancia

    def setDistancia(self, d : float):
        self.distancia = d

    def setLitros(self, l : float):
        self.litros = l

    def getLitros(self):
        return self.litros


class ViagemUI:
    @staticmethod
    def Calculo():
        viagem = Viagem(input("Digite o destino\n"), float(input("Digite a distância em Kms\n")), float(input("Digite quantos litros de combustível você têm\n")))
        print(viagem.ToString())
        print(f"A viagem tem como consumo médio de combustível: {viagem.Consumo():.2f}")
    
    @staticmethod
    def menu():
        i = 1
        while (i != 2):
            i = int(input("1 - Calcular\n2 - Fim\n"))
            if (i == 1):
                ViagemUI.Calculo()
            else:
                break
    @staticmethod
    def main():
        ViagemUI.menu()

ViagemUI.main()
            
            