from abc import ABC, abstractmethod
import random
import enum
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
    def random_enum(cls, enum_cls: type[enum.Enum]):
        return random.choice(list(enum_cls))

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


class BaseMVCTestFactory(ABC):
    @abstractmethod
    def test_get_all(cls, **kwargs):
        pass

    @abstractmethod
    def test_get_one(cls, **kwargs):
        pass

    @abstractmethod
    def test_create(cls, **kwargs):
        pass

    @abstractmethod
    def test_update(cls, **kwargs):
        pass

    @abstractmethod
    def test_delete(cls, **kwargs):
        pass

    def __init_subclass__(cls):
        super().__init_subclass__()

        abstract_methods = {
            name
            for name, value in cls.__dict__.items()
            if getattr(value, "__isabstractmethod__", False)
        }

        # Também verificar na base
        for base in cls.__mro__[1:]:
            if hasattr(base, "__abstractmethods__"):
                abstract_methods |= base.__abstractmethods__

        # Verificar métodos que não foram sobrescritos (são ainda abstratos)
        not_implemented = set()
        for method in abstract_methods:
            # Se a classe não implementou o método
            if method not in cls.__dict__:
                not_implemented.add(method)

        if not_implemented:
            raise TypeError(
                f"Classe {cls.__name__} não implementa os métodos abstratos: "
                f"{', '.join(not_implemented)}"
            )
