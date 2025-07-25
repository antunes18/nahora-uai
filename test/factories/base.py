from abc import ABC, abstractmethod
import random
import string


class BaseTestFactory(ABC):

    @classmethod
    def random_string(cls, length=8):
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    @classmethod
    def random_email(cls):
        return f"{cls.random_string()}@test.com"

    @classmethod
    def random_phone(cls):
        return "".join(random.choices(string.digits, k=13))

    @classmethod
    @abstractmethod
    def create(cls, **kwargs):
        """Retornar um MODEL da Classe"""
        pass

    @classmethod
    @abstractmethod
    def dto(cls, **kwargs):
        """Retornar uma DTO da Classe"""
        pass

    @classmethod
    @abstractmethod
    def update_dto(cls, **kwargs):
        """Retornar uma DTO de UPDATE do Objeto"""
        pass

    @classmethod
    def create_batch(cls, n=5, **kwargs):
        """ Criar uma lista de instancias do MODELO"""
        return [cls.create(**kwargs) for _ in range(n)]

    @classmethod
    def dto_batch(cls, n=5, **kwargs):
        """ Criar uma lista de DTOs do MODELO"""
        return [cls.dto(**kwargs) for _ in range(n)]
