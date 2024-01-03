import pytest
import allure


class TestApi:
    url = "https://petstore.swagger.io/v2"

    @allure.title("Add a new pet to the store in a valid way")
    def test_add_new_pet_200(self, api_client):
        pet = {
            "id": 1,
            "category": {
                "id": 1,
                "name": "category1"
            },
            "name": "doggie",
            "photoUrls": [
                "https://example.com/pet_photo.jpg"
            ],
            "tags": [
                {
                    "id": 1,
                    "name": "tag1"
                }
            ],
            "status": "available"
        }
        response = api_client.post("/pet", pet)
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 200

    @allure.title("Add a new pet to the store without data")
    def test_add_new_pet_405(self, api_client):
        response = api_client.post("/pet", {})
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 405

    @allure.title("Add a new pet to the store without body for request")
    def test_add_new_pet_415(self, api_client):
        response = api_client.post("/pet")
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 415

    @allure.title("Change pet status to 'sold'")
    def test_update_existing_pet_200(self, api_client):
        pet = {
            "id": 1,
            "category": {
                "id": 1,
                "name": "category1"
            },
            "name": "doggie",
            "photoUrls": [
                "https://example.com/pet_photo.jpg"
            ],
            "tags": [
                {
                    "id": 1,
                    "name": "tag1"
                }
            ],
            "status": "sold"
        }
        response = api_client.put("/pet/1", pet)
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 200

    @allure.title("Change pet status to 'lost'")
    def test_update_existing_pet_405(self, api_client):
        pet = {
            "id": 1,
            "category": {
                "id": 1,
                "name": "category1"
            },
            "name": "doggie",
            "photoUrls": [
                "https://example.com/pet_photo.jpg"
            ],
            "tags": [
                {
                    "id": 1,
                    "name": "tag1"
                }
            ],
            "status": "lost"
        }
        response = api_client.put("/pet/1", pet)
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 405

    @allure.title("Change data of nonexistent pet")
    def test_update_nonexistent_pet_404(self, api_client):
        pet = {
            "id": 99,
            "category": {
                "id": 99,
                "name": "category99"
            },
            "name": "doggie99",
            "photoUrls": [
                "https://example.com/pet99_photo.jpg"
            ],
            "tags": [
                {
                    "id": 99,
                    "name": "tag99"
                }
            ],
            "status": "available"
        }
        response = api_client.put("/pet/99", pet)
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 404

    @allure.title("Change data with invalid pet id")
    def test_update_pet_invalid_id_400(self, api_client):
        pet = {
            "id": "p",
            "category": {
                "id": 9,
                "name": "category9"
            },
            "name": "doggie9",
            "photoUrls": [
                "https://example.com/pet99_photo.jpg"
            ],
            "tags": [
                {
                    "id": 9,
                    "name": "tag9"
                }
            ],
            "status": "available"
        }
        response = api_client.put("/pet/p", pet)
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 400

    @allure.title("Change data of pet with ")
    def test_update_nonexistent_pet_404(self, api_client):
        pet = {
            "id": 99,
            "category": {
                "id": 99,
                "name": "category99"
            },
            "name": "doggie99",
            "photoUrls": [
                "https://example.com/pet99_photo.jpg"
            ],
            "tags": [
                {
                    "id": 99,
                    "name": "tag99"
                }
            ],
            "status": "available"
        }
        response = api_client.put("/pet/99", pet)
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 404

    @allure.title("Delete pet")
    def test_delete_pet_200(self, api_client):
        response = api_client.delete("/pet/1")
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 200

    @allure.title("Delete pet once again")
    def test_delete_pet_404(self, api_client):
        response = api_client.delete("/pet/1")
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 404

    @allure.title("Delete pet with invalid id")
    def test_delete_pet_400(self, api_client):
        response = api_client.delete("/pet/p")
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 404
