import json

import requests
import logging
from requests.auth import HTTPBasicAuth

url = "https://reqres.in/"

with requests.Session() as session:
    list_objects = session.get(url)


class UsersWithSession:
    def __init__(self):
        self.session = requests.Session()
        self.url = url
        self.logger = logging.getLogger(__name__)

    def _handle_response(self, response):
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            self.logger.error(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            self.logger.error(f"Request error occurred: {req_err}")
            raise
        except Exception as err:
            self.logger.error(f"An unexpected error occurred: {err}")
            raise

    def get_list_users(self):
        return self.session.get(f'{self.url}{"api/users?page=2"}')

    def get_single_user(self, object_id):
        return self.session.get(f'{self.url}api/users/{object_id}')

    def create_an_user(self):
        urls = self.url + "api/users"
        headers = {"content-type": "application/json"}
        object_body = json.dumps({
            "name": "Tester",
            "job": "Google"})

        response = self.session.post(urls, data=object_body, headers=headers)
        return response

    def update_an_object(self, object_id: object, changed_dict: object):
        headers = {"content-type": "application/json"}
        updated_object = json.dumps(changed_dict)
        response = self.session.patch(f'{self.url}api/users/{object_id}', data=updated_object, headers=headers)
        return response
