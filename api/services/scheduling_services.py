from datetime import date, datetime, timezone, tzinfo

from api.exceptions.generics import EntityNotFound, EntityAlreadyExists, InvalidData, FieldAlreadyUsed
from api.models.dto.scheduling_dto import SchedulingDTO, SchedulingCreateDto
from api.models.scheduling import Scheduling
from api.repository.scheduling_repository import SchedulingReposistory
from api.repository.user_repository import UserRepository


class SchedulingService:
    def __init__(
        self, scheduling_repo: SchedulingReposistory, user_repo: UserRepository
    ):
        self.scheduling_repo = scheduling_repo
        self.user_repo = user_repo

    def create_scheduling(self, dto: SchedulingDTO):
        if (dto.hour < 8) or (14 > dto.hour > 12) or (dto.hour > 18):
            raise InvalidData(
                "A hora deve estar 8 e 12 ou 14 e 18! Horário"
            )

        if dto.date.replace(tzinfo=None) < datetime.today():
            raise InvalidData(
                "Não é possivel registrar para uma data anterior de hoje! Dia"
            )

        try:
            appointment_datetime = datetime.combine(
                dto.date, datetime.min.time()
            ).replace(hour=dto.hour)
        except TypeError:
            raise InvalidData(
                "Data ou hora"
            )

        if appointment_datetime < datetime.now():
            raise InvalidData(
                "Não é possível registrar um agendamento para uma data ou hora no passado. Dada ou Hora"
            )

        existing = self.scheduling_repo.find_scheduling_by_date_and_hour_and_user(
            dto.date, dto.hour, dto.user_id
        )
        user = self.user_repo.get_user(dto.user_id)

        if existing:
            raise EntityAlreadyExists("Scheduling")

        if not user:
            raise EntityNotFound("Usuário")

        scheduling = Scheduling(
            hour=dto.hour,
            date=dto.date,
            name=dto.name,
            user_id=dto.user_id,
            phone=dto.phone,
        )
        return self.scheduling_repo.create(scheduling=scheduling)

    def get_all_schedulings(self, skip: int, limit: int):
        return self.scheduling_repo.find_all(skip, limit)

    def get_all_schedulings_by_user(self, skip: int, limit: int, user_id: int):
        return self.scheduling_repo.find_all_by_user(skip, limit, user_id)

    def get_scheduling(self, scheduling_id: int):
        scheduling = self.scheduling_repo.find_one_scheduling(scheduling_id)

        if not scheduling or scheduling.is_deleted is True:
            raise EntityNotFound("Scheduling")

        return scheduling

    def delete_scheduling(self, scheduling_id: int):
        scheduling = self.scheduling_repo.delete_scheduling(scheduling_id)

        if not scheduling or scheduling.is_deleted is True:
            raise EntityNotFound("Scheduling")

        return {"message": "book deleted"}

    def restore_scheduling(self, scheduling_id: int):
        scheduling = self.scheduling_repo.restore_scheduling(scheduling_id)

        if scheduling:
            return {"message": "book restored"}
        else:
            raise EntityNotFound("Scheduling")

    def update_scheduling(
        self, scheduling_id: int, scheduling_dto: SchedulingDTO
    ):  # Parameter renamed
        existing_scheduling = self.scheduling_repo.find_one_scheduling(
            scheduling_id)

        self.validate_scheduling(scheduling_dto)

        if not existing_scheduling:
            raise EntityNotFound("Scheduling")

        existing_scheduling.hour = scheduling_dto.hour
        existing_scheduling.date = scheduling_dto.date
        existing_scheduling.name = scheduling_dto.name
        existing_scheduling.phone = scheduling_dto.phone

        return self.scheduling_repo.update_scheduling(
            scheduling_id, existing_scheduling
        )

    def validate_scheduling(self, dto: SchedulingDTO):
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
