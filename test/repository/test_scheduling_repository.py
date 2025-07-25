from datetime import timezone

from api.models.dto.scheduling_dto import SchedulingDTO
from api.models.scheduling import Scheduling
from api.models.user import User

from api.repository.scheduling_repository import SchedulingReposistory

from test.dependencies import real_scheduling_repo

from test.mocks.scheduling import (
    mock_scheduling_list,
    mock_scheduling,
    mock_scheduling_update,
)
from test.mocks.user import mock_user


class TestSchedulingRepository:
    def test_create(
        self,
        real_scheduling_repo: SchedulingReposistory,
        mock_scheduling: Scheduling,
        mock_user: User,
    ):
        data = real_scheduling_repo.create(mock_scheduling)

        assert data is not None
        assert data.id == mock_scheduling.id
        assert data.date == mock_scheduling.date
        assert data.hour == mock_scheduling.hour
        assert data.name == mock_scheduling.name
        assert data.phone == mock_scheduling.phone
        assert data.user_id == mock_scheduling.user_id
        assert data.user == mock_scheduling.user
        assert data.is_deleted == mock_scheduling.is_deleted

    def find_scheduling_by_date_and_hour_and_user(
        self,
        real_scheduling_repo: SchedulingReposistory,
        mock_scheduling: Scheduling,
        mock_user: User,
    ):
        real_scheduling_repo.session.add(mock_scheduling)
        real_scheduling_repo.session.commit()

        data = real_scheduling_repo.find_scheduling_by_date_and_hour_and_user(
            date=mock_scheduling.date, hour=mock_scheduling.hour, user_id=mock_user.id
        )
        assert data is not None
        assert data.id == mock_scheduling.id
        assert data.date == mock_scheduling.date
        assert data.hour == mock_scheduling.hour
        assert data.name == mock_scheduling.name
        assert data.phone == mock_scheduling.phone
        assert data.user_id == mock_scheduling.user_id
        assert data.user == mock_scheduling.user
        assert data.is_deleted == mock_scheduling.is_deleted

    def test_find_all(
        self,
        real_scheduling_repo: SchedulingReposistory,
        mock_scheduling: Scheduling,
        mock_scheduling_list: list[Scheduling],
        mock_user: User,
    ):
        real_scheduling_repo.session.add_all(mock_scheduling_list)
        real_scheduling_repo.session.commit()

        data = real_scheduling_repo.find_all(skip=0, limit=10)

        assert data is not None
        # assert len(data) == len(mock_scheduling_list)

    def test_find_one_scheduling(
        self,
        real_scheduling_repo: SchedulingReposistory,
        mock_scheduling: Scheduling,
        mock_user: User,
    ):
        real_scheduling_repo.session.add(mock_scheduling)
        real_scheduling_repo.session.commit()

        data = real_scheduling_repo.find_one_scheduling(
            mock_scheduling.id)

        assert data is not None
        assert data.id == mock_scheduling.id
        assert data.date == mock_scheduling.date
        assert data.hour == mock_scheduling.hour
        assert data.name == mock_scheduling.name
        assert data.phone == mock_scheduling.phone
        assert data.user_id == mock_scheduling.user_id
        assert data.user == mock_scheduling.user
        assert data.is_deleted == mock_scheduling.is_deleted

    def test_delete_scheduling(
        self,
        real_scheduling_repo: SchedulingReposistory,
        mock_scheduling: Scheduling,
        mock_user: User,
    ):
        real_scheduling_repo.session.add(mock_scheduling)
        real_scheduling_repo.session.commit()

        data = real_scheduling_repo.delete_scheduling(mock_scheduling)

        assert data is not None
        assert data.id == mock_scheduling.id
        assert data.date == mock_scheduling.date
        assert data.hour == mock_scheduling.hour
        assert data.name == mock_scheduling.name
        assert data.phone == mock_scheduling.phone
        assert data.user_id == mock_scheduling.user_id
        assert data.user == mock_scheduling.user
        assert data.is_deleted == mock_scheduling.is_deleted

    def test_restore_scheduling(
        self,
        real_scheduling_repo: SchedulingReposistory,
        mock_scheduling: Scheduling,
        mock_user: User,
    ):
        real_scheduling_repo.session.add(mock_scheduling)
        real_scheduling_repo.session.commit()

        data = real_scheduling_repo.restore_scheduling(mock_scheduling)

        assert data is not None
        assert data.id == mock_scheduling.id
        assert data.date == mock_scheduling.date
        assert data.hour == mock_scheduling.hour
        assert data.name == mock_scheduling.name
        assert data.phone == mock_scheduling.phone
        assert data.user_id == mock_scheduling.user_id
        assert data.user == mock_scheduling.user
        assert data.is_deleted == mock_scheduling.is_deleted

    def test_update_scheduling(
        self,
        real_scheduling_repo: SchedulingReposistory,
        mock_scheduling: Scheduling,
        mock_scheduling_update: Scheduling,
        mock_user: User,
    ):
        real_scheduling_repo.session.add(mock_scheduling)
        real_scheduling_repo.session.commit()

        original = real_scheduling_repo.session.get(
            Scheduling, mock_scheduling.id
        )

        original.tenant_id = mock_scheduling_update.tenant_id
        original.date = mock_scheduling_update.date
        original.hour = mock_scheduling_update.hour
        original.name = mock_scheduling_update.name
        original.phone = mock_scheduling_update.phone
        original.user_id = mock_scheduling_update.user_id

        data = real_scheduling_repo.update_scheduling(
            original
        )

        assert data is not None
        assert data.date.replace(
            tzinfo=timezone.utc) == mock_scheduling_update.date.replace(tzinfo=timezone.utc)
        assert data.hour == mock_scheduling_update.hour
        assert data.name == mock_scheduling_update.name
        assert data.phone == mock_scheduling_update.phone
        assert data.user_id == mock_scheduling_update.user_id
