class Produto:
    def __init__(self, id, descricao, preco, estoque, idCategoria):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque
        self.__idCategoria = idCategoria

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_estoque(self):
        return self.__estoque

    def set_estoque(self, estoque):
        self.__estoque = estoque

    def get_idCategoria(self):
        return self.__idCategoria

    def set_idCategoria(self, idCategoria):
        self.__idCategoria = idCategoria

    def __str__(self):
        return (f"ID: {self.__id} | Produto: {self.__descricao} | "
                f"Preço: R$ {self.__preco:.2f} | Estoque: {self.__estoque} | "
                f"Categoria: {self.__idCategoria}")
