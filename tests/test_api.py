import allure
from models.pet import Pet


class TestApi:
    url = "https://petstore.swagger.io/v2"

    # POST requests

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
        if response.ok:
            response_object = response.json()
            with allure.step("Validate response"):
                assert api_client.validate_response(response_object, Pet)

    @allure.title("Add a new pet to the store without data")
    def test_add_new_pet_405(self, api_client):
        response = api_client.post("/pet", {})
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 405

    @allure.title("Add a new pet to the store without body")
    def test_add_new_pet_415(self, api_client):
        response = api_client.post("/pet")
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 415

    # PUT requests

    @allure.title("Change pet status to 'sold'")
    def test_change_status_to_sold_200(self, api_client):
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
        if response.ok:
            response_object = response.json()
            with allure.step("Validate response"):
                assert api_client.validate_response(response_object, Pet)

    @allure.title("Change pet status to 'lost'")
    def test_change_status_to_lost_405(self, api_client):
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

    @allure.title("Change data of non existent pet")
    def test_update_non_existent_pet_404(self, api_client):
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

    @allure.title("Change data of a pet with invalid id")
    def test_update_pet_with_invalid_id_400(self, api_client):
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

    # GET requests

    @allure.title("Find pet by the 'Sold' status")
    def test_find_pet_200(self, api_client):
        params = {
            "status": "sold"
        }
        response = api_client.get("/pet/findByStatus", params)
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 200
        if response.ok:
            response_object = response.json()
            for pet in response_object:
                with allure.step("Validate pet in response"):
                    assert api_client.validate_response(pet, Pet)

    @allure.title("Find pet by the 'Lost' status")
    def test_find_pet_400(self, api_client):
        params = {
            "status": "lost"
        }
        response = api_client.get("/pet/findByStatus", params)
        print(response)
        with allure.step(f"Check status {response.status_code}"):
            assert response.status_code == 400

    # DELETE requests

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
            assert response.status_code == 400
