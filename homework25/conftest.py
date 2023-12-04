import pytest
from homework25.reqres_infra_hw25 import UsersWithSession as User


@pytest.fixture
def session():
    return User()
