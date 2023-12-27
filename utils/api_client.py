import json
import allure
import requests


class ApiClient:
    url = "https://petstore.swagger.io/v2"

    def __init__(self, url):
        self._url = url

    @allure.step("Post request to {path}")
    def post(self, path, data):
        url = self._url + path
        return requests.post(url, data)

    @allure.step("Put request to {path}")
    def put(self, path, data):
        url = self._url + path
        return requests.put(url, data)

    @allure.step("Delete request to {path}")
    def delete(self, path):
        url = self._url + path
        return requests.delete(url)
