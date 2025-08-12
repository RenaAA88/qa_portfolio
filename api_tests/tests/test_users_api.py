import pytest
import requests
import json

BASE_URL = "https://petstore.swagger.io/v2"


def print_test_header(test_name):
    
    print(f"\n{'=' * 50}")
    print(f"ТЕСТ: {test_name}")
    print('=' * 50)
def print_request_response(request_method, url, response, request_data=None):	
    
    print(f"\n[ЗАПРОС]")
    print(f"Метод: {request_method}")
    print(f"URL: {url}")
    
    if request_data:
        print("Тело запроса:")
        print(json.dumps(request_data, indent=2, ensure_ascii=False))
    
    print(f"\n[ОТВЕТ]")
    print(f"Статус код: {response.status_code}")
    if response.text:
        try:
            print("Тело ответа:")
            print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        except ValueError:
            print(response.text)

class TestPetstoreAPI:
    def test_create_and_get_pet(self):
        print_test_header("Создание и получение питомца")
        
         
        new_pet = {
            "id": 987654321,
            "name": "TestDog",
            "status": "available"
        }
        
     
        post_url = f"{BASE_URL}/pet"
        post_response = requests.post(post_url, json=new_pet)
        print_request_response("POST", post_url, post_response, new_pet)
        assert post_response.status_code == 200
        
        pet_id = new_pet["id"]
        get_url = f"{BASE_URL}/pet/{pet_id}"
        get_response = requests.get(get_url)
        print_request_response("GET", get_url, get_response)
        
        pet_id = new_pet["id"]
        get_url = f"{BASE_URL}/pet/{pet_id}"
        get_response = requests.get(get_url)
        print_request_response("GET", get_url, get_response)

