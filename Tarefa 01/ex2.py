class Pais:
    def __init__(self, nome, populacao, area):
        if (populacao <= 0 or area <= 0 or nome == ""):
            print("Valores devem ser válidos")
        else:
            self.nome = nome
            self.populacao = populacao
            self.area = area

    def Pais(self, nome, populacao, area):
        if (populacao <= 0 or area <= 0 or nome == ""):
                print("Valores devem ser válidos")
        else:
            self.nome = nome
            self.populacao = populacao
            self.area = area
    
    def Densidade(self):
        return self.populacao / self.area

    def ToString(self):
        return f"O país {self.nome} tem população de {self.populacao} habitantes e área de {self.area}Km²"

    def getNome(self):
        return self.nome
    
    def setNome(self, n):
        self.nome = n

    def getPopulacao(self):
        return self.populacao

    def setPopulacao(self, p):
        self.populacao = p
    
    def getArea(self):
        return self.area

    def setArea(self, a):
        self.area = a
    
class PaisUI:
    @staticmethod
    def Calculo():
        pais = Pais(input("Digite o nome do país\n"), int(input("Digite a população do país\n")), float(input("Digite a área do país em Km²\n")))
        print(pais.ToString())
        print(f"O país tem densidade demográfica de: {pais.Densidade():.2f} habitantes por Km²")
    
    @staticmethod
    def menu():
        i = 1
        while (i != 2):
            i = int(input("1 - Calcular\n2 - Fim\n"))
            if (i == 1):
                PaisUI.Calculo()
            else:
                break
    @staticmethod
    def main():
        PaisUI.menu()

PaisUI.main()