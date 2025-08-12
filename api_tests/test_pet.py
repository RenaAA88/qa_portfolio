import pytest
import requests
import allure

@allure.feature("PetStore API")
class TestPetAPI:
    @allure.title("Получение информации о питомце")
    def test_get_pet(self):
        pet_id = 1
        response = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")
        
        assert response.status_code == 200
        assert response.json()["id"] == pet_id