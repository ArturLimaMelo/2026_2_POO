import hashlib
import secrets
import hmac


class Cliente:
    def __init__(
        self, id, nome, email, telefone,
        senha=None, salt=None, senha_hash=None
    ):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

        self.__salt = salt or secrets.token_hex(16)

        if senha_hash is not None:
            self.__senha_hash = senha_hash
        elif senha is not None:
            self.__senha_hash = self._gerar_hash(senha)
        else:
            self.__senha_hash = ""

    def _gerar_hash(self, senha):
        return hashlib.pbkdf2_hmac(
            "sha256",
            senha.encode("utf-8"),
            bytes.fromhex(self.__salt),
            100_000
        ).hex()

    def verificar_senha(self, senha):
        hash_tentativa = self._gerar_hash(senha)
        return hmac.compare_digest(
            self.__senha_hash,
            hash_tentativa
        )

    def get_senha_hash(self):
        return self.__senha_hash

    def get_salt(self):
        return self.__salt

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def __str__(self):
        return (
            f"ID: {self.__id} | Nome: {self.__nome} | "
            f"E-mail: {self.__email} | Telefone: {self.__telefone}"
        )