import requests
from homework_24.example_api_hw24 import Phone


def test_get_single_obj():
    object = Phone.get_an_object(2)
    assert object.status_code == 200


def test_get_an_single_name():
    object = Phone.get_an_object(2)
    print(object.json())
    assert object.json()['name'] == "Apple iPhone 12 Mini, 256GB, Blue"
    assert object.status_code == 200


def test_check_name_for_id_3():
    response = Phone.get_all_object()
    data = response.json()

    # Ищем объект с ID 3
    object_with_id_3 = next((obj for obj in data if obj.get('id') == '3'))

    actual_name = object_with_id_3.get('name')
    assert response.status_code == 200
    assert actual_name == "Apple iPhone 12 Pro Max"


def test_get_an_obj_id_name():
    object = Phone.get_an_object(2)
    print(object.json())
    assert object.json()['name'] == "Apple iPhone 12 Mini, 256GB, Blue", object.status_code == 200


def test_get_an_obj_id_len():
    object = Phone.get_an_object(1)
    print(object.json())
    assert len(object.json()) == 3
    assert object.status_code == 200


def test_get_single_obj_len():
    object = Phone.get_all_object()
    print(object.json())
    assert len(object.json()) == 13
    assert object.status_code == 200


def test_get_obj_ids_len():
    object = Phone.get_object_by_ids([2, 4, 7])
    print(object.json())
    assert len(object.json()) == 3
    assert object.status_code == 200


def test_create_single_object():
    response = Phone.create_an_object()
    assert response.json()["data"]["CPU model"] == "Intel Core i9"
    assert response.status_code == 200


def test_create_car():
    response = Phone.create_an_car1()
    print(response.json())
    assert response.json()["data"]["wheels size"] == "R 22"
    assert response.status_code == 200


def test_update_mac_color():
    created_mac = Phone.create_an_object()
    updated_mac_dict = created_mac.json()
    updated_mac_dict['data']['colour'] = 'Gold'
    updated_mac_dict.pop('createdAt')
    updated_mac_response_object = Phone.update_an_object(updated_mac_dict['id'], updated_mac_dict)
    print(created_mac.json())
    print(updated_mac_response_object.json())
    assert updated_mac_response_object.json()['data']['colour'] == 'Gold'


def test_update_mac_price():
    created_mac = Phone.create_an_object()
    updated_mac_dict = created_mac.json()
    updated_mac_dict['data']['price'] = 1200.5
    updated_mac_response_object = Phone.update_an_object(updated_mac_dict['id'], updated_mac_dict)
    assert updated_mac_response_object.json()['data']['price'] == 1200.5


def test_update_mac_CPU():
    created_mac2 = Phone.create_an_object()
    updated_mac2_dict = created_mac2.json()
    updated_mac2_dict['data']['price'] = 999
    updated_mac2_response_object = Phone.update_an_object(updated_mac2_dict['id'], updated_mac2_dict)
    assert updated_mac2_response_object.json()['data']['price'] == 999


def test_update_BMW():
    created_car = Phone.create_an_car1()
    updated_car_dict = created_car.json()
    updated_car_dict['name'] = "BMW i8"
    updated_car_response_object = Phone.update_an_object(updated_car_dict['id'], updated_car_dict)
    print(updated_car_response_object.json())
    assert updated_car_response_object.json()['name'] == "BMW i8"


def test_patch_BMW():
    created_car = Phone.create_an_car1()
    updated_car_dict = {'name': 'BMW X9'}
    updated_car_response_object = Phone.patch_an_object(created_car.json()['id'], updated_car_dict)
    print(created_car.json())
    print(updated_car_response_object.json())
    assert updated_car_response_object.json()['name'] == 'BMW X9'
    assert updated_car_response_object.status_code == 200


def test_delete_car():
    created_car = Phone.create_an_object()
    response_deleted_car = Phone.del_an_object(created_car.json()['id'])
    assert response_deleted_car.json()['message'] == f"Object with id = {created_car.json()['id']} has been deleted."
