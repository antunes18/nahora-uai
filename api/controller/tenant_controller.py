from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.core.database import get_db
from api.core.jwt_bearer import JwtBearer
from api.exceptions.message import GenericError

from api.models.tenant import Tenant
from api.models.dto.tenant_dto import TenantCreateDTO, TenantResponseDTO, TenantUpdateDTO

from api.repository.tenant_repository import TenantRepository
from api.services.tenant_services import TenantService


router = APIRouter(prefix="/tenant", tags=["Tenant"])


def get_tenant_repo(db: Session = Depends(get_db)) -> TenantRepository:
    return TenantRepository(session=db)


def get_tenant_services(
    tenant_repo: TenantRepository = Depends(get_tenant_repo),
) -> TenantService:
    return TenantService(tenant_repo=tenant_repo)


@router.post(
    "/",
    response_model=TenantResponseDTO,
    response_model_exclude_unset=True,
    status_code=200,
    responses={
        200: {
            "model": TenantResponseDTO,
            "description": "Tenant foi Criado com Sucesso!",
        },
        422: {
            "model": GenericError,
            "description": "Dados estão incorretos",
        },
        404: {
            "model": GenericError,
            "description": "Informação não encontrada!",
        },
    },
    # dependencies=[Depends(JwtBearer())],
)
def create(
    dto: TenantCreateDTO,
    services: TenantService = Depends(get_tenant_services),
):
    return services.create(tenant_create_dto=dto)


@router.get(
    "/",
    response_model=List[TenantResponseDTO],
    response_model_exclude_unset=True,
    responses={
        201: {
            "model": List[TenantResponseDTO],
            "description": "Lista de Tenants",
        },
        400: {
            "model": GenericError,
            "description": "Tenants Não Encontradas",
        },
        500: {"model": GenericError, "description": "Error no Servidor"},
    },
    status_code=200,
    # dependencies=[Depends(JwtBearer())],
)
def get_all(skip: int = 0, limit: int = 100, service: TenantService = Depends(get_tenant_services)):
    return service.get_all(skip=skip, limit=limit)


@router.get(
    "/{id}",
    status_code=200,
    response_model=TenantResponseDTO,
    response_model_exclude_unset=True,
    responses={
        200: {
            "model": TenantResponseDTO,
            "description": "Informações da Tenant",
        },
        404: {
            "model": GenericError,
            "description": "Tenant Não Encontrada",
        },
        500: {"model": GenericError, "description": "Error no Servidor"},
    },
    # dependencies=[Depends(JwtBearer())],
)
def get_one(id: int, services: TenantService = Depends(get_tenant_services)):
    return services.get_one(id)


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
            "description": "Informação Não Encontrado",
        },
        500: {"model": GenericError, "description": "Erro no Servidor"},
    },
    # dependencies=[Depends(JwtBearer())],
)
def update(
    id: int,
    update_data: TenantUpdateDTO,
    services: TenantService = Depends(get_tenant_services),
):
    return services.update(tenant_id=id, update_tenant=update_data)


@router.delete(
    "/{id}",
    status_code=204,
    response_model_exclude_unset=True,
    responses={
        204: {
            "description": "Tenant Deletada com sucesso!",
        },
        404: {
            "model": GenericError,
            "description": "Informação Não Encontrado!",
        },
        500: {"model": GenericError, "description": "Error no Servidor!"},
    },
    # dependencies=[Depends(JwtBearer())],
)
def delete(id: int, services: TenantService = Depends(get_tenant_services)):
    return services.delete(tenant_id=id)
