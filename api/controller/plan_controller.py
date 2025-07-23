from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from api.core.database import get_db
from api.core.jwt_bearer import JwtBearer
from api.exceptions.message import GenericError

from api.models.plan import Plan
from api.models.dto.plan_dto import PlanCreateDTO, PlanUpdateDTO, PlanResponseDTO

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
    response_model=PlanResponseDTO,
    response_model_exclude_unset=True,
    status_code=201,
    responses={
        201: {
            "model": PlanResponseDTO,
            "description": "Plano foi Criado com Sucesso!",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": " não encontrada!",
        },

        422: {
            "model": GenericError,
            "description": "Dados estão incorretos",
        },

    },
    # dependencies=[Depends(JwtBearer())],
)
def create(
    obj: PlanCreateDTO,
    services: PlanService = Depends(get_plan_services),
):
    return services.create(obj)


@router.get(
    "/",
    status_code=200,
    response_model=List[PlanResponseDTO],
    response_model_exclude_unset=True,
    responses={
        200: {
            "model": List[PlanResponseDTO],
            "description": "Lista de Planos",
        },

        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },

        404: {
            "model": GenericError,
            "description": "Plano Não Encontrado",
        },

    },
    # dependencies=[Depends(JwtBearer())],
)
def get_all(skip: int = 0, limit: int = 100, services: PlanService = Depends(get_plan_services)):
    return services.get_all(skip=skip, limit=limit)


@router.get(
    "/{id}",
    status_code=200,
    response_model=PlanResponseDTO,
    response_model_exclude_unset=True,
    responses={
        200: {
            "model": PlanResponseDTO,
            "description": "Informações do Plano",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": "Plano Não Encontrada",
        },
    },
    # dependencies=[Depends(JwtBearer())],
)
def get_one(id: int, services: PlanService = Depends(get_plan_services)):
    return services.get_one(plan_id=id)


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
            "description": "Plano Não Encontrado",
        },

    },
    # dependencies=[Depends(JwtBearer())],
)
def update(
    id: int,
    update_data: PlanUpdateDTO,
    services: PlanService = Depends(get_plan_services),
):
    return services.update(plan_id=id, update_plan=update_data)


@router.delete(
    "/{id}",
    status_code=204,
    response_model_exclude_unset=True,
    responses={
        204: {
            "description": "Informação Deletada com sucesso!",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },
        404: {
            "model": GenericError,
            "description": "Plano Não Encontrado!",
        },
    },
    # dependencies=[Depends(JwtBearer())],
)
def delete(id: int, services: PlanService = Depends(get_plan_services)):
    return services.delete(plan_id=id)
