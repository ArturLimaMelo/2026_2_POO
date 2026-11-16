from Service import Service


class UI:
    service = Service()

    @staticmethod
    def menu():
        print("\n========== MENU ==========")
        print(" 1 - Inserir cliente")
        print(" 2 - Listar clientes")
        print(" 3 - Atualizar cliente")
        print(" 4 - Excluir cliente")
        print(" 5 - Inserir categoria")
        print(" 6 - Listar categorias")
        print(" 7 - Atualizar categoria")
        print(" 8 - Excluir categoria")
        print(" 9 - Inserir produto")
        print("10 - Listar produtos")
        print("11 - Atualizar produto")
        print("12 - Excluir produto")
        print("13 - Reajustar preços dos produtos")
        print(" 0 - Finalizar")
        print("==========================")

    @staticmethod
    def ler_id():
        return int(input("ID: "))

    @staticmethod
    def cliente_inserir():
        print("\\n--- Novo cliente ---")
        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        ok = UI.service.cliente_inserir(nome, email, telefone)
        print("Cliente cadastrado." if ok else "Não foi possível cadastrar.")

    @staticmethod
    def cliente_listar():
        print("\\n--- Clientes ---")
        clientes = UI.service.cliente_listar()
        if not clientes:
            print("Nenhum cliente cadastrado.")
        for cliente in clientes:
            print(cliente)

    @staticmethod
    def cliente_atualizar():
        id = UI.ler_id()
        if UI.service.cliente_listar_id(id) is None:
            print("Cliente não encontrado.")
            return
        nome = input("Novo nome: ")
        email = input("Novo e-mail: ")
        telefone = input("Novo telefone: ")
        ok = UI.service.cliente_atualizar(id, nome, email, telefone)
        print("Cliente atualizado." if ok else "Falha ao atualizar.")

    @staticmethod
    def cliente_excluir():
        ok = UI.service.cliente_excluir(UI.ler_id())
        print("Cliente excluído." if ok else "Cliente não encontrado.")

    @staticmethod
    def categoria_inserir():
        descricao = input("Descrição da categoria: ")
        ok = UI.service.categoria_inserir(descricao)
        print("Categoria cadastrada." if ok else "Falha ao cadastrar.")

    @staticmethod
    def categoria_listar():
        print("\\n--- Categorias ---")
        categorias = UI.service.categoria_listar()
        if not categorias:
            print("Nenhuma categoria cadastrada.")
        for categoria in categorias:
            print(categoria)

    @staticmethod
    def categoria_atualizar():
        id = UI.ler_id()
        if UI.service.categoria_listar_id(id) is None:
            print("Categoria não encontrada.")
            return
        descricao = input("Nova descrição: ")
        ok = UI.service.categoria_atualizar(id, descricao)
        print("Categoria atualizada." if ok else "Falha ao atualizar.")

    @staticmethod
    def categoria_excluir():
        ok = UI.service.categoria_excluir(UI.ler_id())
        print("Categoria excluída." if ok else "Categoria não encontrada.")

    @staticmethod
    def produto_inserir():
        print("\\n--- Novo produto ---")
        descricao = input("Descrição: ")
        preco = float(input("Preço: R$ ").replace(",", "."))
        estoque = int(input("Estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("ID da categoria: "))
        ok = UI.service.produto_inserir(descricao, preco, estoque, id_categoria)
        print("Produto cadastrado." if ok else "Categoria inexistente; produto não cadastrado.")

    @staticmethod
    def produto_listar():
        print("\\n--- Produtos ---")
        produtos = UI.service.produto_listar()
        if not produtos:
            print("Nenhum produto cadastrado.")
        for produto in produtos:
            print(produto)

    @staticmethod
    def produto_atualizar():
        id = UI.ler_id()
        if UI.service.produto_listar_id(id) is None:
            print("Produto não encontrado.")
            return
        descricao = input("Nova descrição: ")
        preco = float(input("Novo preço: R$ ").replace(",", "."))
        estoque = int(input("Novo estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Novo ID da categoria: "))
        ok = UI.service.produto_atualizar(id, descricao, preco, estoque, id_categoria)
        print("Produto atualizado." if ok else "Categoria inexistente; produto não atualizado.")

    @staticmethod
    def produto_excluir():
        ok = UI.service.produto_excluir(UI.ler_id())
        print("Produto excluído." if ok else "Produto não encontrado.")

    @staticmethod
    def produto_reajustar():
        percentual = float(input("Percentual (ex.: 10 para aumento ou -10 para promoção): ").replace(",", "."))
        UI.service.produto_reajustar(percentual)
        print("Preços atualizados.")

    @staticmethod
    def main():
        while True:
            UI.menu()
            try:
                opcao = int(input("Escolha uma opção: "))
                operacoes = {
                    1: UI.cliente_inserir,
                    2: UI.cliente_listar,
                    3: UI.cliente_atualizar,
                    4: UI.cliente_excluir,
                    5: UI.categoria_inserir,
                    6: UI.categoria_listar,
                    7: UI.categoria_atualizar,
                    8: UI.categoria_excluir,
                    9: UI.produto_inserir,
                    10: UI.produto_listar,
                    11: UI.produto_atualizar,
                    12: UI.produto_excluir,
                    13: UI.produto_reajustar
                }
                if opcao == 0:
                    print("Aplicação finalizada.")
                    break
                operacao = operacoes.get(opcao)
                if operacao:
                    operacao()
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
            except Exception as erro:
                print(f"Ocorreu um erro: {erro}")


if __name__ == "__main__":
    UI.main()
