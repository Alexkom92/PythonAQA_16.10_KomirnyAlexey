from homework25.reqres_infra_hw25 import UsersWithSession as User
import pytest


def test_get_list_users():
    session = User()
    object = session.get_list_users()
    print(object.json())
    assert object.status_code == 200


def test_get_single_user():
    session = User()
    object = session.get_single_user(2)
    assert object.status_code == 200


def test_create_user():
    session = User()
    response = session.create_an_user()
    assert response.status_code == 201


def test_create_user1():
    session = User()
    response = session.create_an_user()
    assert response.json()["name"] == "Tester"


@pytest.mark.parametrize("new_job", ["Driver", "Artist"])
def test_update_user(session, new_job):
    # Создание пользователя
    created_user_data = session.create_an_user()
    print(created_user_data.json())
    assert created_user_data.status_code == 201  # Проверка наличия ключа "status_code"

    # Получение актуальных данных о пользователе
    object_id = created_user_data.json()["id"]

    # Печать созданного пользователя
    print("Created user:", object_id)

    updated_user_dict = created_user_data.json()
    updated_user_dict.pop('createdAt')
    updated_user_dict['job'] = new_job
    update_user_response = session.update_an_object(object_id, updated_user_dict)
    print(update_user_response.json())
    assert update_user_response.json()['job'] == new_job



