class Cliente:
    def __init__(self, nome, cpf, limite):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_limite(limite)
        self.__socio = None
    def set_nome(self, nome):
        if nome == "" : raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_cpf(self, cpf)
        if cpf <= 0 : raise ValueError("Cpf inválido")
        self.__cpf = cpf
    def set_limite(self, limite)
        if limite <= 0: raise ValueError("Limite inválido")
        self.__limite = limite
    def set_socio(self, socio):
        if socio == "": raise ValueError("Sócio deve ser informado")
        self.__socio = socio 
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_limite(self):
        return self.__limite
    def get_socio(self):
        return self.__socio    
    