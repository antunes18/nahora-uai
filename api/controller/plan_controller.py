from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.core.database import get_db

from api.models.plan import Plan
from api.repository.plan_repository import PlanRepository
from api.services.plan_services import PlanService


router = APIRouter(prefix="/plan", tags=["Plan"])


def get_plan_repo(db: Session = Depends(get_db)) -> PlanRepository:
    return PlanRepository(session=db)


def get_plan_services(
    plan_repo: PlanRepository = Depends(get_plan_repo),
) -> PlanService:
    return PlanService(plan_repo=plan_repo)


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
