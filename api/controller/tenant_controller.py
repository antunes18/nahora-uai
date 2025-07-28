from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.core.database import get_db
from api.core.jwt_bearer import JwtBearer
from api.exceptions.message import GenericError

from api.models.dto.tenant_dto import TenantCreateDTO, TenantResponseDTO, TenantUpdateDTO

from api.models.dto.user_dto import UserResponseDTO
from api.models.dto.scheduling_dto import SchedulingResponseDTO

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
    status_code=201,
    response_model=TenantResponseDTO,
    response_model_exclude_unset=True,
    responses={
        201: {
            "model": TenantResponseDTO,
            "description": "Tenant foi Criado com Sucesso!",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": "Tenant não encontrada!",
        },
        422: {
            "model": GenericError,
            "description": "Dados estão incorretos",
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
    status_code=200,
    response_model=List[TenantResponseDTO],
    response_model_exclude_unset=True,
    responses={
        201: {
            "model": List[TenantResponseDTO],
            "description": "Lista de Tenants",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": "Tenants não encontradas!",
        }
    },
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
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": "Tenant não encontrada!",
        }
    },
    # dependencies=[Depends(JwtBearer())],
)
def get_one(id: int, services: TenantService = Depends(get_tenant_services)):
    return services.get_one(id)


@router.get(
    "/{id}/users",
    status_code=200,
    response_model=List[UserResponseDTO],
    response_model_exclude_unset=True,
    responses={
        201: {
            "model": List[UserResponseDTO],
            "description": "Lista de Users da Tenant",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": "Tenants não encontradas!",
        }
    },
    # dependencies=[Depends(JwtBearer())],
)
def get_all_users(id: int = 0, service: TenantService = Depends(get_tenant_services)):
    return service.get_all_users(tenant_id=id)


@router.get(
    "/{id}/schedulings",
    status_code=200,
    response_model=List[SchedulingResponseDTO],
    response_model_exclude_unset=True,
    responses={
        201: {
            "model": List[SchedulingResponseDTO],
            "description": "Lista de Users da Tenant",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": "Tenants não encontradas!",
        }
    },
    # dependencies=[Depends(JwtBearer())],
)
def get_all_schedulings(id: int = 0, service: TenantService = Depends(get_tenant_services)):
    return service.get_all_schedulings(tenant_id=id)


@router.put(
    "/{id}",
    status_code=204,
    response_model_exclude_unset=True,
    responses={
        204: {
            "description": "Dados Atualizados com Sucesso",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": "Tenant não encontrada!",
        }
    }
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
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": "Tenant não encontrada!",
        }
    },
    # dependencies=[Depends(JwtBearer())],
)
def delete(id: int, services: TenantService = Depends(get_tenant_services)):
    return services.delete(tenant_id=id)
