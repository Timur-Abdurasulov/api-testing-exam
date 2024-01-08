import allure


class TestApi:
    url = "https://petstore.swagger.io/v2"

    def test_find_pet_200(self, api_client):
        params = {"status": "sold"}
        response = api_client.get("/pet/findByStatus", params)
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 200
        response_object = response.json()
        print(response_object)
        for pet in response_object:
            print(pet)

    def test_find_pet_400(self, api_client):
        params = {
            "status": "lost"
        }
        response = api_client.get("/pet/findByStatus", params)
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 200
        response_object = response.json()
        print(response_object)
