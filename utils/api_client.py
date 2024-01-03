import allure
import requests
from pydantic import BaseModel


class ApiClient:
    url = "https://petstore.swagger.io/v2"

    def __init__(self, url):
        self._url = url

    # @allure.step("Post request to {path}")
    # def post(self, path, data):
    #     url = self._url + path
    #     return requests.post(url, data)
    #
    # @allure.step("Put request to {path}")
    # def put(self, path, data):
    #     url = self._url + path
    #     return requests.put(url, data)

    @allure.step("{method} request to {path}")
    def make_request(self, method, path, data):
        url = self._url + path
        request_method = getattr(requests, method)
        return request_method(url, data)

    @allure.step("Delete request to {path}")
    def delete(self, path):
        url = self._url + path
        return requests.delete(url)

    @allure.step("Validate response data")
    def validate_data(self, result: object, model: BaseModel):
        return model.model_validate(result)