import pytest
from homework25.reqres_infra_hw25 import UsersWithSession as User
from unittest.mock import MagicMock
from requests.exceptions import HTTPError

@pytest.fixture
def session():
    return User()


@pytest.fixture
def mock_response():
    response = MagicMock()
    response.json.return_value = {"data": "example_data"}
    return response
