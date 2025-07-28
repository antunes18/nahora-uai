from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from api.core.database import get_db
from api.exceptions.message import GenericError

from api.models.subscription import Subscription
from api.models.dto.subscription_dto import SubscriptionCreateDTO, SubscriptionResponseDTO, SubscriptionUpdateDTO

from api.repository.subscription_repository import SubscriptionRepository
from api.repository.plan_repository import PlanRepository
from api.repository.tenant_repository import TenantRepository

from api.services.subscription_services import SubscriptionService


router = APIRouter(prefix="/subscription", tags=["Subscription"])


def get_subscription_repo(db: Session = Depends(get_db)) -> SubscriptionRepository:
    return SubscriptionRepository(session=db)


def get_plan_repo(db: Session = Depends(get_db)) -> PlanRepository:
    return PlanRepository(session=db)


def get_tenant_repo(db: Session = Depends(get_db)) -> TenantRepository:
    return TenantRepository(session=db)


def get_subscription_services(
    subscription_repo: SubscriptionRepository = Depends(get_subscription_repo),
    plan_repo: PlanRepository = Depends(get_plan_repo),
    tenant_repo: TenantRepository = Depends(get_tenant_repo)
) -> SubscriptionService:
    return SubscriptionService(subscription_repo=subscription_repo, plan_repo=plan_repo, tenant_repo=tenant_repo)


@router.post(
    "/",
    status_code=201,
    response_model=SubscriptionCreateDTO,
    response_model_exclude_unset=True,
    responses={
        201: {
            "model": SubscriptionResponseDTO,
            "description": "Subscription foi Criado com Sucesso!",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": "Subscription não encontrada!",
        },
        422: {
            "model": GenericError,
            "description": "Dados estão incorretos",
        },
    },
    # dependencies=[Depends(JwtBearer())],
)
def create(
    obj: SubscriptionCreateDTO,
    services: SubscriptionService = Depends(get_subscription_services),
):
    return services.create(obj)


@router.get(
    "/",
    status_code=200,
    response_model=List[SubscriptionResponseDTO],
    response_model_exclude_unset=True,
    responses={
        201: {
            "model": List[SubscriptionResponseDTO],
            "description": "Lista de Subscriptions",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": "Subscriptions não encontradas!",
        }
    },
    # dependencies=[Depends(JwtBearer())],
)
def get_all(skip: int = 0, limit: int = 100, services: SubscriptionService = Depends(get_subscription_services)):
    return services.get_all(skip=skip, limit=limit)


@router.get(
    "/{id}",
    status_code=200,
    response_model=SubscriptionResponseDTO,
    response_model_exclude_unset=True,
    responses={
        200: {
            "model": SubscriptionResponseDTO,
            "description": "Informações da Subscription",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": "Subscription não encontrada!",
        }
    },
    # dependencies=[Depends(JwtBearer())],
)
def get_one(id: int, services: SubscriptionService = Depends(get_subscription_services)):
    return services.get_one(subscription_id=id)


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
    update_data: SubscriptionUpdateDTO,
    services: SubscriptionService = Depends(get_subscription_services),
):
    return services.update(subscription_id=id, update_subscription=update_data)


@router.delete(
    "/{id}",
    status_code=204,
    response_model_exclude_unset=True,
    responses={
        204: {
            "description": "Subscription Deletada com sucesso!",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": "Subscription não encontrada!",
        }
    },
    # dependencies=[Depends(JwtBearer())],
)
def delete(id: int, services: SubscriptionService = Depends(get_subscription_services)):
    return services.delete(subscription_id=id)
