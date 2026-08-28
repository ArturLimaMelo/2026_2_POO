# Entidade
class ContaBancaria:
    def __init__(self):
        self.titular = "sem nome"
        self.numero = "sem número"
        self.__saldo = 0              # Encapsulamento
    def depositar(self, valor):
        if valor >= 0: 
            self.__saldo += valor
        else:
            #print("Valor deve ser positivo")   
            raise ValueError("Valor deve ser positivo")  
    def sacar(self, valor):
        if valor >= 0 and self.__saldo >= valor:
            self.__saldo -= valor
        else:
            #print("Saldo Insuficiente")     
            raise ValueError("Valor deve ser positivo ou saldo insuficiente")  
    def consultar_saldo(self):
        return self.__saldo

# Interface com o usuário
x = ContaBancaria()
x.titular = "Eduardo"
x.numero = "123-0"

#print(x.saldo)     saldo da conta está encapsulado
#print(x.__saldo)

print(x.titular, x.numero, x.consultar_saldo())
x.depositar(1000)
print(x.titular, x.numero, x.consultar_saldo())
x.sacar(1200)
print(x.titular, x.numero, x.consultar_saldo())
