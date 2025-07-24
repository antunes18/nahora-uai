from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.core.jwt_bearer import JwtBearer
from api.core.database import get_db
from api.exceptions.message import GenericError
from api.repository.scheduling_repository import SchedulingReposistory
from api.repository.user_repository import UserRepository
from api.services.scheduling_services import SchedulingService
from api.models.dto.scheduling_dto import SchedulingDTO, SchedulingCreateDto, SchedulingUpdateDTO


router = APIRouter(prefix="/scheduling", tags=["Scheduling"])


def get_scheduling_repo(db: Session = Depends(get_db)) -> SchedulingReposistory:
    return SchedulingReposistory(session=db)


def get_user_repo(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(session=db)


def get_scheduling_services(
    user_repo: UserRepository = Depends(get_user_repo),
    scheduling_repo: SchedulingReposistory = Depends(get_scheduling_repo),
) -> SchedulingService:
    return SchedulingService(scheduling_repo=scheduling_repo, user_repo=user_repo)


@router.post(
    "/",
    response_model=SchedulingDTO,
    response_model_exclude_unset=True,
    status_code=201,
    responses={
        201: {
            "model": SchedulingDTO,
            "description": "Scheduling foi Criado com Sucesso!",
        },
        400: {
            "model": GenericError,
            "description": "Dados estão incorretos",
        },
        404: {
            "model": GenericError,
            "description": "Usuário com esse id não existe!",
        },
    },
    dependencies=[Depends(JwtBearer())],
)
def create_Scheduling(
    scheduling: SchedulingCreateDto,
    services: SchedulingService = Depends(get_scheduling_services),
):
    return services.create_scheduling(scheduling)


@router.get(
    "/",
    response_model=List[SchedulingDTO],
    response_model_exclude_unset=True,
    responses={
        200: {
            "model": List[SchedulingDTO],
            "description": "Lista de Schedulings",
        }
    },
    status_code=200,
    dependencies=[Depends(JwtBearer())],
)
def get_all_scheduling(
    skip: int = 0,
    limit: int = 10,
    services: SchedulingService = Depends(get_scheduling_services),
):
    return services.get_all_schedulings(skip, limit)


@router.get(
    "/user/{user_id}",
    response_model=List[SchedulingDTO],
    response_model_exclude_unset=True,
    responses={
        200: {
            "model": List[SchedulingDTO],
            "description": "Lista de Schedulings do usuario",
        }
    },
    status_code=200,
    dependencies=[Depends(JwtBearer())],
)
def get_all_schedulings_by_user(
    user_id: int,
    skip: int = 0,
    limit: int = 10,
    services: SchedulingService = Depends(get_scheduling_services),
):
    return services.get_all_schedulings_by_user(skip, limit, user_id)


@router.get(
    "/{id}",
    response_model=SchedulingDTO,
    response_model_exclude_unset=True,
    status_code=200,
    responses={
        200: {
            "model": SchedulingDTO,
            "description": "Informações do Scheduling",
        },
        404: {
            "model": GenericError,
            "description": "Scheduling Não Encontrado",
        },
    },
    dependencies=[Depends(JwtBearer())],
)
def get_one_scheduling(
    id: int, services: SchedulingService = Depends(get_scheduling_services)
):
    return services.get_scheduling(id)


@router.delete(
    "/delete/{id}",
    status_code=204,
    response_model_exclude_unset=True,
    responses={
        204: {
            "description": "Scheduling excluído",
        },
        404: {
            "model": GenericError,
            "description": "Scheduling Não Encontrado",
        },
    },
    dependencies=[Depends(JwtBearer())],
)
def delete_scheduling(
    id: int, services: SchedulingService = Depends(get_scheduling_services)
):
    return services.delete_scheduling(id)


@router.put(
    "/restore/{id}",
    status_code=204,
    response_model_exclude_unset=True,
    responses={
        204: {
            "description": "Scheduling restaurado",
        },
        404: {
            "model": GenericError,
            "description": "Scheduling Não Encontrado",
        },
    },
    dependencies=[Depends(JwtBearer())],
)
def restore_scheduling(
    id: int, services: SchedulingService = Depends(get_scheduling_services)
):
    return services.restore_scheduling(id)


@router.put(
    "/update/{id}",
    status_code=204,
    response_model_exclude_unset=True,
    responses={
        200: {
            "description": "Scheduling Atualizado",
        },
        404: {
            "model": GenericError,
            "description": "Scheduling Não Encontrado",
        },
    },
    dependencies=[Depends(JwtBearer())],
)
def update_scheduling(
    id: int,
    scheduling: SchedulingUpdateDTO,
    services: SchedulingService = Depends(get_scheduling_services),
):
    return services.update_scheduling(id, scheduling)
