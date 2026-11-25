from Cliente import Cliente
from Categoria import Categoria
from Produto import Produto
from ClienteDAO import ClienteDAO
from CategoriaDAO import CategoriaDAO
from ProdutoDAO import ProdutoDAO
from PedidoDAO import PedidoDAO

class Service:
    def __init__(self):
        self.cliente_dao = ClienteDAO()
        self.categoria_dao = CategoriaDAO()
        self.produto_dao = ProdutoDAO()
        self.pedido_dao = PedidoDAO()

        self.cliente_dao.Abrir()
        self.categoria_dao.Abrir()
        self.produto_dao.Abrir()
        self.pedido_dao.Abrir()

        self._criar_admin()


    def _criar_admin(self):
        admin = self.cliente_dao.Listar_Email("admin")

        if admin is None:
            id = self._proximo_id(self.cliente_dao.Listar())

            administrador = Cliente(
                id,
                "Administrador",
                "admin",
                "",
                "admin123"
            )

            self.cliente_dao.Inserir(administrador)

    @staticmethod
    def _proximo_id(lista):
        if not lista:
            return 1
        return max(obj.get_id() for obj in lista) + 1


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


    def autenticar(self, email, senha):
        cliente = self.cliente_dao.Listar_Email(email.strip())

        if cliente is None:
            return None

        if not cliente.verificar_senha(senha):
            return None

        return cliente




    def cadastrar_cliente(self, nome, email, telefone, senha):
        if not nome.strip() or not email.strip():
            return False

        if not telefone.strip() or not senha:
            return False

        if self.cliente_dao.Listar_Email(email.strip()) is not None:
            return False

        id = self._proximo_id(self.cliente_dao.Listar())

        cliente = Cliente(
            id,
            nome.strip(),
            email.strip(),
            telefone.strip(),
            senha
        )

        return self.cliente_dao.Inserir(cliente)




    def pedido_listar(self):
        return self.pedido_dao.Listar()


    def pedido_listar_id(self, id):
        return self.pedido_dao.Listar_Id(id)


    def pedido_listar_cliente(self, id_cliente):
        return self.pedido_dao.Listar_Cliente(id_cliente)


    def pedido_inserir(self, pedido):
        return self.pedido_dao.Inserir(pedido)