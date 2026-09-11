class Conversor:
    def __init__(self, num : int):
        self.num = num

    def Conversor(self, num : int):
        self.num = num

    def setNum(self, num : int):
        self.num = num
    
    def getNum(self):
        return self.num

    def Binario(self):
        return str(bin(self.num)[2:])

    def ToString(self):
        return f"O número decimal {self.num} em binário é escrito como {bin(self.num)[2:]}"

teste = Conversor(int(input()))
print(teste.ToString())
print(teste.Binario())