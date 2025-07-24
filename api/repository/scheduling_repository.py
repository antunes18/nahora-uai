import datetime
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import extract

from api.models.scheduling import Scheduling


class SchedulingReposistory:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, scheduling: Scheduling) -> Scheduling:
        self.session.add(scheduling)
        self.session.commit()
        self.session.refresh(scheduling)
        return scheduling

    def find_scheduling_by_date_and_hour_and_user(
        self, date: datetime.date, hour: int, user_id: int
    ) -> Scheduling | None:
        return (
            self.session.query(Scheduling)
            .filter(
                extract("year", Scheduling.date) == date.year,
                extract("month", Scheduling.date) == date.month,
                extract("day", Scheduling.date) == date.day,
                Scheduling.hour == hour,
                Scheduling.user_id == user_id,
                Scheduling.is_deleted == False,
            )
            .first()
        )

    def find_all(self, skip: int, limit: int) -> List[Scheduling]:
        return (
            self.session.query(Scheduling)
            .filter(Scheduling.is_deleted == False)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def find_all_by_user(self, skip: int, limit: int, user_id: int) -> List[Scheduling]:
        return (
            self.session.query(Scheduling)
            .filter(
                Scheduling.is_deleted == False,
                Scheduling.user_id == user_id
            )
            .offset(skip)
            .limit(limit)
            .all()
        )

    def find_one_scheduling(self, id: int) -> Scheduling | None:
        return self.session.query(Scheduling).filter(Scheduling.id == id).first()

    def delete_scheduling(self, scheduling: Scheduling) -> Scheduling | None:
        scheduling.is_deleted = True
        self.session.commit()
        self.session.refresh(scheduling)
        return scheduling

    def restore_scheduling(self, scheduling: Scheduling) -> Scheduling | None:
        scheduling.is_deleted = False
        self.session.commit()
        self.session.refresh(scheduling)
        return scheduling

    def update_scheduling(self, scheduling: Scheduling) -> Scheduling | None:
        self.session.commit()
        self.session.refresh(scheduling)
        return scheduling
