from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from api.core.database import get_db
from api.core.jwt_bearer import JwtBearer

from api.exceptions.message import GenericError


from api.models.invoice import Invoice
from api.models.dto.invoice_dto import InvoiceCreateDTO, InvoiceResponseDTO, InvoiceUpdateDTO

from api.repository.invoice_repository import InvoiceRepository
from api.repository.subscription_repository import SubscriptionRepository

from api.services.invoice_services import InvoiceService


router = APIRouter(prefix="/invoice", tags=["Invoice"])


def get_invoice_repo(db: Session = Depends(get_db)) -> InvoiceRepository:
    return InvoiceRepository(session=db)


def get_subscription_repo(db: Session = Depends(get_db)) -> SubscriptionRepository:
    return SubscriptionRepository(session=db)


def get_invoice_services(
    invoice_repo: InvoiceRepository = Depends(get_invoice_repo),
    subscription_repo: SubscriptionRepository = Depends(get_subscription_repo)
) -> InvoiceService:
    return InvoiceService(invoice_repo=invoice_repo, subscription_repo=subscription_repo)


@router.post(
    "/",
    status_code=201,
    response_model=InvoiceResponseDTO,
    response_model_exclude_unset=True,
    responses={
        201: {
            "model": InvoiceResponseDTO,
            "description": "Fatura foi Criado com Sucesso!",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },

        422: {
            "model": GenericError,
            "description": "Dados estão incorretos",
        },

    },
    # dependencies=[Depends(JwtBearer())],
)
def create(
    obj: InvoiceCreateDTO,
    services: InvoiceService = Depends(get_invoice_services),
):
    return services.create(obj)


@router.get(
    "/",
    status_code=200,
    response_model=List[InvoiceResponseDTO],
    response_model_exclude_unset=True,
    responses={
        200: {
            "model": List[InvoiceResponseDTO],
            "description": "Lista de Faturas",
        },

        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },

        404: {
            "model": GenericError,
            "description": "Fatura Não Encontrada!",
        },

    },
    # dependencies=[Depends(JwtBearer())],
)
def get_all(skip: int = 0, limit: int = 100, services: InvoiceService = Depends(get_invoice_services)):
    return services.get_all(skip=skip, limit=limit)


@router.get(
    "/{id}",
    status_code=200,
    response_model=InvoiceResponseDTO,
    response_model_exclude_unset=True,
    responses={
        200: {
            "model": InvoiceResponseDTO,
            "description": "Retornar Informações da Fatura",
        },
        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },

        404: {
            "model": GenericError,
            "description": "Fatura Não Encontrada!",
        },

    },
    # dependencies=[Depends(JwtBearer())],
)
def get_one(id: int, services: InvoiceService = Depends(get_invoice_services)):
    return services.get_one(invoice_id=id)


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
            "description": "Fatura Não Encontrada!",
        },

    },
    # dependencies=[Depends(JwtBearer())],
)
def update(
    id: int,
    update_data: InvoiceUpdateDTO,
    services: InvoiceService = Depends(get_invoice_services),
):
    return services.update(invoice_id=id, update_invoice=update_data)


@router.delete(
    "/{id}",
    status_code=204,
    response_model_exclude_unset=True,
    responses={
        204: {
            "description": "Fatura Deletada com sucesso!",
        },

        403: {
            "model": GenericError,
            "description": "Usuário Não Autenticado!",
        },

        404: {
            "model": GenericError,
            "description": "Fatura Não Encontrada!",
        },

    },
    # dependencies=[Depends(JwtBearer())],
)
def delete(id: int, services: InvoiceService = Depends(get_invoice_services)):
    return services.delete(invoice_id=id)
