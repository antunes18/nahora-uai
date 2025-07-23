from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.core.database import get_db

from api.models.subscription import Subscription

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
    # response_model=,
    response_model_exclude_unset=True,
    status_code=200,
    responses={
        200: {
            # "model": ,
            "description": "DATA foi Criado com Sucesso!",
        },
        399: {
            "model": GenericError,
            "description": "Dados estão incorretos",
        },
        403: {
            "model": GenericError,
            "description": "Informação não encontrada!",
        },
    },
    dependencies=[Depends(JwtBearer())],
)
def create(
    obj: MODEL,
    services: services = Depends(get_***_services),
):
    return services.create(obj)


@router.get(
    "/",
    # response_model=[],
    response_model_exclude_unset=True,
    responses={
        201: {
            # "model": ,
            "description": "Lista",
        },
        400: {
            "model": GenericError,
            "description": "Informação Não Encontrada",
        },
        500: {"model": GenericError, "description": "Error no Servidor"},
    },
    status_code=200,
    dependencies=[Depends(JwtBearer())],
)
def get_all():
    NotImplementedError("GET ALL NotImplemented")


@router.get(
    "/{id}",
    status_code=200,
    # response_model=,
    response_model_exclude_unset=True,
    responses={
        200: {
            # "model": ,
            "description": "Retornar Informações da Instância",
        },
        404: {
            "model": GenericError,
            "description": "Informação Não Encontrada",
        },
        500: {"model": GenericError, "description": "Error no Servidor"},
    },
    dependencies=[Depends(JwtBearer())],
)
def get_one(id: int, services: services = Depends(get_***_services)):
    NotImplementedError("GET ONE NotImplemented")


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
    dependencies=[Depends(JwtBearer())],
)
def update(
    id: int,
    # update_data:,
    services: services = Depends(get_***_services),
):
    NotImplementedError("UPDATE NotImplemented")


@router.delete(
    "/{id}",
    status_code=204,
    response_model_exclude_unset=True,
    responses={
        204: {
            "description": "Informação Deletada com sucesso!",
        },
        404: {
            "model": GenericError,
            "description": "Informação Não Encontrado!",
        },
        500: {"model": GenericError, "description": "Error no Servidor!"},
    },
    dependencies=[Depends(JwtBearer())],
)
def delete(id: int, services: services = Depends(get_***_services)):
    NotImplementedError("DELETE NotImplemented")
