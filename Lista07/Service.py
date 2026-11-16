from Cliente import Cliente
from Categoria import Categoria
from Produto import Produto
from ClienteDAO import ClienteDAO
from CategoriaDAO import CategoriaDAO
from ProdutoDAO import ProdutoDAO


class Service:
    def __init__(self):
        self.cliente_dao = ClienteDAO()
        self.categoria_dao = CategoriaDAO()
        self.produto_dao = ProdutoDAO()

        # Carrega os dados persistidos nos arquivos JSON.
        self.cliente_dao.Abrir()
        self.categoria_dao.Abrir()
        self.produto_dao.Abrir()

    @staticmethod
    def _proximo_id(lista):
        if not lista:
            return 1
        return max(obj.get_id() for obj in lista) + 1

    # CLIENTES
    def cliente_inserir(self, nome, email, fone):
        id = self._proximo_id(self.cliente_dao.Listar())
        cliente = Cliente(id, nome, email, fone)
        return self.cliente_dao.Inserir(cliente)

    def cliente_listar(self):
        return self.cliente_dao.Listar()

    def cliente_listar_id(self, id):
        return self.cliente_dao.Listar_Id(id)

    def cliente_atualizar(self, id, nome, email, fone):
        return self.cliente_dao.Atualizar(id, nome, email, fone)

    def cliente_excluir(self, id):
        return self.cliente_dao.Excluir(id)

    # CATEGORIAS
    def categoria_inserir(self, descricao):
        id = self._proximo_id(self.categoria_dao.Listar())
        categoria = Categoria(id, descricao)
        return self.categoria_dao.Inserir(categoria)

    def categoria_listar(self):
        return self.categoria_dao.Listar()

    def categoria_listar_id(self, id):
        return self.categoria_dao.Listar_Id(id)

    def categoria_atualizar(self, id, descricao):
        return self.categoria_dao.Atualizar(id, descricao)

    def categoria_excluir(self, id):
        return self.categoria_dao.Excluir(id)

    # PRODUTOS
    def produto_inserir(self, descricao, preco, estoque, idCategoria):
        if self.categoria_listar_id(idCategoria) is None:
            return False
        id = self._proximo_id(self.produto_dao.Listar())
        produto = Produto(id, descricao, preco, estoque, idCategoria)
        return self.produto_dao.Inserir(produto)

    def produto_listar(self):
        return self.produto_dao.Listar()

    def produto_listar_id(self, id):
        return self.produto_dao.Listar_Id(id)

    def produto_atualizar(self, id, descricao, preco, estoque, idCategoria):
        if self.categoria_listar_id(idCategoria) is None:
            return False
        return self.produto_dao.Atualizar(id, descricao, preco, estoque, idCategoria)

    def produto_excluir(self, id):
        return self.produto_dao.Excluir(id)

    def produto_reajustar(self, percentual):
        fator = 1 + percentual / 100
        for produto in self.produto_dao.Listar():
            novo_preco = produto.get_preco() * fator
            self.produto_dao.Atualizar(
                produto.get_id(),
                produto.get_descricao(),
                round(novo_preco, 2),
                produto.get_estoque(),
                produto.get_idCategoria()
            )
        return True
