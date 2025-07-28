from fastapi import APIRouter, Depends
from typing import List

from api.core.jwt_bearer import JwtBearer
from api.core.dependecies import get_user_services
from api.exceptions.message import GenericError

from api.services.auth_services import UserServices

from api.models.dto.user_dto import (
    UserResponseDTO,
    UserUpdateDTO,
)

router = APIRouter(prefix="/user", tags=["Users"])


@router.get(
    "/",
    response_model=List[UserResponseDTO],
    response_model_exclude_unset=True,
    responses={
        201: {
            "model": List[UserResponseDTO],
            "description": "Lista de Usuários",
        },
        400: {
            "model": GenericError,
            "description": "Nenhum Usuário Cadastrado",
        },
        500: {"model": GenericError, "description": "Error no Servidor"},
    },
    status_code=200,
    dependencies=[Depends(JwtBearer())],
)
def get_all_users(
    skip: int = 0,
    limit: int = 100,
    services: UserServices = Depends(get_user_services),
) -> List[UserResponseDTO]:
    return services.get_all(skip=skip, limit=limit)


@router.get(
    "/{id}",
    status_code=200,
    response_model=UserResponseDTO,
    response_model_exclude_unset=True,
    responses={
        200: {
            "model": UserResponseDTO,
            "description": "Informações do Usuário",
        },
        404: {
            "model": GenericError,
            "description": "Usuário Não Encontrado",
        },
        500: {"model": GenericError, "description": "Error no Servidor"},
    },
    dependencies=[Depends(JwtBearer())],
)
def get_user(id: int, services: UserServices = Depends(get_user_services)):
    return services.get_user(id)


@router.put(
    "/{id}",
    status_code=204,
    response_model_exclude_unset=True,
    responses={
        204: {
            "description": "Dados Atualizados com Sucesso",
        },
        404: {
            "model": GenericError,
            "description": "Usuário Não Encontrado",
        },
        500: {"model": GenericError, "description": "Error no Servidor"},
    },
    dependencies=[Depends(JwtBearer())],
)
def update_user(
    id: int,
    update_data: UserUpdateDTO,
    services: UserServices = Depends(get_user_services),
):
    return services.update_user(user_id=id, update_user=update_data)


@router.delete(
    "/{id}",
    status_code=204,
    response_model_exclude_unset=True,
    responses={
        204: {
            "description": "Usuário Deletado com sucesso!",
        },
        404: {
            "model": GenericError,
            "description": "Usuário Não Encontrado!",
        },
        500: {"model": GenericError, "description": "Error no Servidor!"},
    },
    dependencies=[Depends(JwtBearer())],
)
def delete_user(id: int, services: UserServices = Depends(get_user_services)):
    return services.delete_user(user_id=id)


@router.put(
    "/restore/{id}",
    status_code=204,
    response_model_exclude_unset=True,
    responses={
        204: {
            "description": "Usuário Restaurado",
        },
        404: {
            "model": GenericError,
            "description": "Usuário Não Encontrado",
        },
        500: {"model": GenericError, "description": "Error no Servidor"},
    },
    dependencies=[Depends(JwtBearer())],
)
def restore_user(id: int, services: UserServices = Depends(get_user_services)):
    return services.restore_user(user_id=id)
