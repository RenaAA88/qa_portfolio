from email.mime import application
import json
import requests # type: ignore
import allure

#def test_get_pet_status():
    name ="dog"    
    resp = requests.get("https://petstore.swagger.io/v2/pet/1")
    
    assert 200 == resp.status_code
    assert "application/json" == resp.headers ["content-type"]
    assert name == resp.json()["name"]
    
@allure.title("Создание зверушки") 
@allure.description("Создание питомца с помощью petstore") 
@allure.epic("Эпоха разработки")
@allure.feature ("Функционал") 
@allure.story("История")
@allure.issue("Проблема")
@allure.severity(allure.severity_level.MINOR)
#def test_create_pet():
    json = {
             "name": "snoop doggie",
            "status": "available"
            }
    
    resp = requests.post("https://petstore.swagger.io/v2/pet/", json=json)
    assert 200 == resp.status_code
    
    assert json["name"] == resp.json()["name"]