import requests
import json

url = "https://api.restful-api.dev/objects"


class Phone:
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def get_all_object():
        return requests.get(url)

    def get_an_object(object_id):
        return requests.get(f'{url}/{object_id}')

    def get_object_by_ids(list_id_number: list):
        ids = ''
        for object_id in list_id_number:
            if object_id != list_id_number[-1]:
                ids += f'id={object_id}&'
            else:
                ids += f'id={object_id}'
        return requests.get(f"{url}?{ids}")

    def create_an_object():
        headers = {"content-type": "application/json"}
        object_body = json.dumps({"name": "Apple MacBook Pro 16",
                                  "data": {
                                      "year": 2019,
                                      "price": 1849.99,
                                      "CPU model": "Intel Core i9",
                                      "Hard disk size": "1 TB"}})
        response = requests.post(url, data=object_body, headers=headers)
        return response

    def create_an_car1():
        headers = {"content-type": "application/json"}
        object_body = json.dumps({"name": "BMW X5",
                                  "data": {
                                      "year": 2015,
                                      "price": 5525.89,
                                      "engine": "4.4l",
                                      "wheels size": "R 22"}})
        response = requests.post(url, data=object_body, headers=headers)
        return response

    def update_an_object(object_id, changed_dict):
        headers = {"content-type":"application/json"}
        updated_object = json.dumps(changed_dict)
        return requests.put(f'{url}/{object_id}', data=updated_object,headers=headers)