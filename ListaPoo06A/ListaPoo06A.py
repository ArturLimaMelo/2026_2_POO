import json
import os


class Cliente:
    def __init__(self, id, n, e, f):
        self.__id = id
        self.__nome = n
        self.__email = e
        self.__fone = f

    def To_Dict(self):
        return {
            "ID": self.__id,
            "Nome": self.__nome,
            "E-mail": self.__email,
            "Fone": self.__fone
        }

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | E-mail: {self.__email} | Fone: {self.__fone}"

    def Get_Id(self):
        return self.__id

    def Set_Id(self, id):
        self.__id = id

    def Get_Nome(self):
        return self.__nome

    def Set_Nome(self, nome):
        self.__nome = nome

    def Get_Email(self):
        return self.__email

    def Set_Email(self, email):
        self.__email = email

    def Get_Fone(self):
        return self.__fone

    def Set_Fone(self, fone):
        self.__fone = fone


class ClienteDAO:
    objetos = []

    def Inserir(self, obj):
        if self.Listar_Id(obj.Get_Id()) is not None:
            return

        self.objetos.append(obj)

    def Listar(self):
        return self.objetos.copy()

    def Listar_Id(self, id):
        for obj in self.objetos:
            if obj.Get_Id() == id:
                return obj

        return None

    def Atualizar(self, obj):
        cliente = self.Listar_Id(obj.Get_Id())

        if cliente is None:
            return

        cliente.Set_Nome(obj.Get_Nome())
        cliente.Set_Email(obj.Get_Email())
        cliente.Set_Fone(obj.Get_Fone())

    def Excluir(self, obj):
        cliente = self.Listar_Id(obj.Get_Id())

        if cliente is not None:
            self.objetos.remove(cliente)

    def Abrir(self):
        if not os.path.exists("clientes.json"):
            return

        with open("clientes.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        self.objetos.clear()

        for item in dados:
            cliente = Cliente(
                item["ID"],
                item["Nome"],
                item["E-mail"],
                item["Fone"]
            )

            self.objetos.append(cliente)

    def Salvar(self):
        dados = [obj.To_Dict() for obj in self.objetos]

        with open("clientes.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

class UI:
    @staticmethod
    def Menu():
        print("\n===== SISTEMA DE CLIENTES =====")
        print("1 - Listar clientes")
        print("2 - Inserir cliente")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("0 - Finalizar")

        return int(input("Escolha uma opção: "))

    @staticmethod
    def Cliente_Listar():
        dao = ClienteDAO()
        clientes = dao.Listar()

        if not clientes:
            print("\nNenhum cliente cadastrado.")
            return

        for cliente in clientes:
            print(str(cliente))

    @staticmethod
    def Cliente_Inserir():
        dao = ClienteDAO()

        try:
            id = int(input("ID: "))
        except ValueError:
            print("ID inválido.")
            return

        if dao.Listar_Id(id) is not None:
            print("Já existe um cliente com esse ID.")
            return

        nome = input("Nome: ")
        email = input("E-mail: ")
        fone = input("Telefone: ")

        cliente = Cliente(id, nome, email, fone)

        dao.Inserir(cliente)
        dao.Salvar()

        print("Cliente inserido com sucesso.")

    @staticmethod
    def Cliente_Atualizar():
        dao = ClienteDAO()

        try:
            id = int(input("ID do cliente que deseja atualizar: "))
        except ValueError:
            print("ID inválido.")
            return

        cliente = dao.Listar_Id(id)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        nome = input(f"Nome ({cliente.Get_Nome()}): ")
        email = input(f"E-mail ({cliente.Get_Email()}): ")
        fone = input(f"Telefone ({cliente.Get_Fone()}): ")

        atualizado = Cliente(
            id,
            nome if nome else cliente.Get_Nome(),
            email if email else cliente.Get_Email(),
            fone if fone else cliente.Get_Fone()
        )

        dao.Atualizar(atualizado)
        dao.Salvar()

        print("Cliente atualizado com sucesso.")

    @staticmethod
    def Cliente_Excluir():
        dao = ClienteDAO()

        try:
            id = int(input("ID do cliente que deseja excluir: "))
        except ValueError:
            print("ID inválido.")
            return

        cliente = dao.Listar_Id(id)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        dao.Excluir(cliente)
        dao.Salvar()

        print("Cliente excluído com sucesso.")

    @staticmethod
    def Main():
        dao = ClienteDAO()
        dao.Abrir()

        while True:
            try:
                opcao = UI.Menu()
            except ValueError:
                print("Digite uma opção válida.")
                continue

            if opcao == 1:
                UI.Cliente_Listar()
            elif opcao == 2:
                UI.Cliente_Inserir()
            elif opcao == 3:
                UI.Cliente_Atualizar()
            elif opcao == 4:
                UI.Cliente_Excluir()
            elif opcao == 0:
                print("Aplicação finalizada.")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    UI.Main()