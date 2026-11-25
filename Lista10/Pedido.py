from datetime import datetime


class Pedido:
    def __init__(
        self,
        id,
        id_cliente,
        nome_cliente,
        itens,
        data=None,
        status="Confirmado"
    ):
        self.__id = id
        self.__id_cliente = id_cliente
        self.__nome_cliente = nome_cliente
        self.__itens = itens
        self.__data = data or datetime.now().isoformat()
        self.__status = status

    def get_id(self):
        return self.__id

    def get_id_cliente(self):
        return self.__id_cliente

    def get_nome_cliente(self):
        return self.__nome_cliente

    def get_itens(self):
        return self.__itens

    def get_data(self):
        return self.__data

    def get_status(self):
        return self.__status

    def get_total(self):
        return sum(
            item["preco"] * item["quantidade"]
            for item in self.__itens
        )

    def __str__(self):
        return (
            f"Pedido: {self.__id} | "
            f"Cliente: {self.__nome_cliente} | "
            f"Total: R$ {self.get_total():.2f} | "
            f"Status: {self.__status}"
        )