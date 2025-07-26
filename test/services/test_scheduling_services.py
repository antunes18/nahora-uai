from unittest.mock import Mock

from api.models.dto.scheduling_dto import SchedulingDTO
from api.models.scheduling import Scheduling
from api.models.user import User
from api.services.scheduling_services import SchedulingService

from test.factories.base import BaseMVCTestFactory

from test.dependencies import (
    mock_user_repo,
    mock_scheduling_repo,
    mock_scheduling_services,
    mock_tenant_repo
)

from test.mocks.scheduling import (
    mock_scheduling,
    mock_scheduling_create,
    mock_scheduling_list,
    mock_scheduling_update,
)
from test.mocks.user import mock_user


class TestSchedulingServices(BaseMVCTestFactory):
    def test_create(
        self,
        mock_scheduling_services: SchedulingService,
        mock_scheduling_repo: Mock,
        mock_user_repo: Mock,
        mock_scheduling: Scheduling,
        mock_scheduling_create: SchedulingDTO,
    ):
        mock_scheduling_repo.find_scheduling_by_date_and_hour_and_user.return_value = None
        mock_user_repo.get_user.return_value = mock_user
        mock_scheduling_repo.create.return_value = mock_scheduling

        response = mock_scheduling_services.create_scheduling(
            mock_scheduling_create)

        assert response is not None
        assert response.hour == mock_scheduling.hour
        assert response.date == mock_scheduling.date
        assert response.name == mock_scheduling.name
        assert response.phone == mock_scheduling.phone
        assert response.user_id == mock_scheduling.user_id

    def test_get_all(
        self,
        mock_scheduling_repo: Mock,
        mock_scheduling_services: SchedulingService,
        mock_user: User,
    ):
        mock_scheduling_repo.find_all.return_value = mock_scheduling_list

        response = mock_scheduling_services.get_all_schedulings(
            skip=0, limit=10)

        assert response is not None

    def test_get_one(
        self,
        mock_scheduling_repo: Mock,
        mock_scheduling_services: SchedulingService,
        mock_scheduling: Scheduling,
    ):
        mock_scheduling_repo.find_one_scheduling.return_value = mock_scheduling

        response = mock_scheduling_services.get_scheduling(mock_scheduling.id)

        assert response is not None

        assert response.hour == mock_scheduling.hour
        assert response.date == mock_scheduling.date
        assert response.name == mock_scheduling.name
        assert response.phone == mock_scheduling.phone
        assert response.user_id == mock_scheduling.user_id

    def test_delete(
        self,
        mock_scheduling_repo: Mock,
        mock_scheduling_services: SchedulingService,
        mock_scheduling: Scheduling,
    ):
        mock_scheduling_repo.delete_scheduling(
            mock_scheduling.id
        ).return_value = mock_scheduling
        response = mock_scheduling_services.delete_scheduling(
            mock_scheduling.id)
        assert response is not None

    def test_restore(
        self,
        mock_scheduling_repo: Mock,
        mock_scheduling_services: SchedulingService,
        mock_scheduling: Scheduling,
    ):
        mock_scheduling_repo.restore_scheduling(
            mock_scheduling.id
        ).return_value = mock_scheduling

        response = mock_scheduling_services.restore_scheduling(
            mock_scheduling.id)
        assert response is not None

    def test_update(
        self,
        mock_scheduling_repo: Mock,
        mock_scheduling_services: SchedulingService,
        mock_scheduling: Scheduling,
        mock_scheduling_update: SchedulingDTO,
    ):
        mock_scheduling_repo.find_one_scheduling.return_value = mock_scheduling
        mock_scheduling_repo.update_scheduling.return_value = (
            mock_scheduling_update
        )

        response = mock_scheduling_services.update_scheduling(
            mock_scheduling.id, mock_scheduling_update
        )

        assert response is not None
        assert response.hour == mock_scheduling_update.hour
        assert response.date == mock_scheduling_update.date
        assert response.name == mock_scheduling_update.name
        assert response.phone == mock_scheduling_update.phone
        assert response.user_id == mock_scheduling_update.user_id
