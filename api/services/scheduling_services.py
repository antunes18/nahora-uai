from datetime import date, datetime, timezone, tzinfo
from typing import List

from api.exceptions.generics import EntityNotFound, EntityAlreadyExists, InvalidData, FieldAlreadyUsed
from api.models.dto.scheduling_dto import SchedulingDTO, SchedulingCreateDto
from api.models.scheduling import Scheduling
from api.repository.scheduling_repository import SchedulingReposistory
from api.repository.user_repository import UserRepository


class SchedulingService:
    def __init__(
        self, scheduling_repo: SchedulingReposistory, user_repo: UserRepository
    ) -> None:
        self.scheduling_repo = scheduling_repo
        self.user_repo = user_repo

    def create_scheduling(self, dto: SchedulingDTO) -> Scheduling:

        self.validate_scheduling(dto)

        if self.scheduling_repo.find_scheduling_by_date_and_hour_and_user(date=dto.date, hour=dto.hour, user_id=dto.user_id):
            raise EntityAlreadyExists("Scheduling")

        if not self.user_repo.get_user(user_id=dto.user_id):
            raise EntityNotFound("Usuário")

        scheduling: Scheduling = Scheduling(
            hour=dto.hour,
            date=dto.date,
            name=dto.name,
            user_id=dto.user_id,
            phone=dto.phone,
        )
        return self.scheduling_repo.create(scheduling=scheduling)

    def get_all_schedulings(self, skip: int, limit: int) -> List[Scheduling]:
        return self.scheduling_repo.find_all(skip, limit)

    def get_all_schedulings_by_user(self, skip: int, limit: int, user_id: int) -> List[Scheduling]:
        return self.scheduling_repo.find_all_by_user(skip, limit, user_id)

    def get_scheduling(self, scheduling_id: int) -> Scheduling:
        scheduling: Scheduling = self.scheduling_repo.find_one_scheduling(
            scheduling_id)

        if not scheduling or scheduling.is_deleted is True:
            raise EntityNotFound("Scheduling")

        return scheduling

    def delete_scheduling(self, scheduling_id: int) -> Scheduling:
        scheduling: Scheduling = self.scheduling_repo.find_one_scheduling(
            id=scheduling_id)

        if not scheduling or scheduling.is_deleted is True:
            raise EntityNotFound("Scheduling")

        return self.scheduling_repo.delete_scheduling(scheduling=scheduling)

    def restore_scheduling(self, scheduling_id: int) -> Scheduling:
        scheduling: Scheduling = self.scheduling_repo.find_one_scheduling(
            id=scheduling_id)

        if not scheduling:
            raise EntityNotFound("Scheduling")

        return self.scheduling_repo.restore_scheduling(scheduling)

    def update_scheduling(
        self, scheduling_id: int, scheduling_dto: SchedulingDTO
    ) -> Scheduling:
        existing_scheduling: Scheduling = self.scheduling_repo.find_one_scheduling(
            scheduling_id)

        if not existing_scheduling or existing_scheduling.is_deleted == True:
            raise EntityNotFound("Scheduling")

        self.validate_scheduling(scheduling_dto)

        try:
            existing_scheduling.hour = scheduling_dto.hour
            existing_scheduling.date = scheduling_dto.date
            existing_scheduling.name = scheduling_dto.name
            existing_scheduling.phone = scheduling_dto.phone

            return self.scheduling_repo.update_scheduling(
                existing_scheduling
            )
        except Exception:
            raise InvalidData("Dados de Scheduling")

    def validate_scheduling(self, dto: SchedulingDTO) -> None:
        if (dto.hour < 8) or (14 > dto.hour > 12) or (dto.hour > 18):
            raise InvalidData(
                "A hora deve estar 8 e 12 ou 14 e 18! Horário"
            )

        if dto.date.replace(tzinfo=None) < datetime.today():
            raise InvalidData(
                "Não é possivel registrar para uma data anterior de hoje! Data"
            )

        try:
            appointment_datetime = datetime.combine(
                dto.date, datetime.min.time()
            ).replace(hour=dto.hour)
        except TypeError:
            raise InvalidData(
                "Data ou hora inválida para o agendamento. Horário"
            )

        if appointment_datetime < datetime.now():
            raise InvalidData(
                "Não é possível registrar um agendamento para uma data ou hora no passado. Horário"
            )
