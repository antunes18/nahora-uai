from fastapi import Depends
from api.repository.user_repository import UserRepository
from api.repository.scheduling_repository import SchedulingReposistory

from api.services.auth_services import UserServices
from api.services.scheduling_services import SchedulingService
from sqlalchemy.orm import Session
from api.core.database import get_db


def get_scheduling_repo(db: Session = Depends(get_db)) -> SchedulingReposistory:
    return SchedulingReposistory(session=db)


def get_user_repo(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(session=db)


def get_user_services(
    user_repo: UserRepository = Depends(get_user_repo),
) -> UserServices:
    return UserServices(user_repo=user_repo)


def get_scheduling_services(
    user_repo: UserRepository = Depends(get_user_repo),
    scheduling_repo: SchedulingReposistory = Depends(get_scheduling_repo),
) -> SchedulingService:
    return SchedulingService(scheduling_repo=scheduling_repo, user_repo=user_repo)
