from fastapi import HTTPException
from pydantic import BaseModel


class GenericError(BaseModel):
    message: str
    status_code: int


class AppException(HTTPException):
    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)


# Exceções genéricas reutilizáveis com personalização
class EntityAlreadyExists(AppException):
    def __init__(self, entity_name: str = "Recurso"):
        super().__init__(status_code=400, detail=f"{entity_name} já existe!")


class EntityNotFound(AppException):
    def __init__(self, entity_name: str = "Recurso"):
        super().__init__(status_code=404, detail=f"{
            entity_name} não encontrado!")


class InvalidData(AppException):
    def __init__(self, entity_name: str = "Dados"):
        super().__init__(status_code=422, detail=f"{entity_name} inválidos!")


class UnauthorizedAction(AppException):
    def __init__(self, detail: str = "Ação não autorizada."):
        super().__init__(status_code=403, detail=detail)


class FieldAlreadyUsed(AppException):
    def __init__(self, field_name: str = "Campo"):
        super().__init__(status_code=400, detail=f"{
            field_name} já está em uso!")
