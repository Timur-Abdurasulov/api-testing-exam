import allure
import requests
from pydantic import BaseModel


class ApiClient:
    url = "https://petstore.swagger.io/v2"

    def __init__(self, url):
        self._url = url

    # @allure.step("{method} request to {path}")
    # def make_request(self, method, path, data):
    #     url = self._url + path
    #     request_method = getattr(requests, method)
    #     return request_method(url, json=data)

    @allure.step("Post request to {path}")
    def post(self, path, data=None):
        if data is None:
            data = {}
        url = self._url + path
        return requests.post(url, json=data)

    @allure.step("Put request to {path}")
    def put(self, path, data=None):
        if data is None:
            data = {}
        url = self._url + path
        return requests.put(url, json=data)

    @allure.step("Get request to {path}")
    def get(self, path, params=None):
        if params is None:
            params = []
        url = self._url + path
        return requests.get(url, params)

    @allure.step("Delete request to {path}")
    def delete(self, path):
        url = self._url + path
        return requests.delete(url)

    @allure.step("Validate response data")
    def validate_response(self, result: object, model: BaseModel):
        return model.model_validate(result)
