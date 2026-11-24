class Categoria:
    def __init__(self, id, descricao):
        self.__id = id
        self.__descricao = descricao

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def __str__(self):
        return f"ID: {self.__id} | Descrição: {self.__descricao}"
