import requests
import pytest
import time

@pytest.fixture(scope="session")
def base_url():
    return "https://automationexercise.com/api"

# response = requests.get("https://automationexercise.com/api/productsList")
# response2 = requests.post("https://automationexercise.com/api/productsList")
# print(response.status_code)
# print(response.json()["products"][0]["id"])

def test_products(base_url):
    response = requests.get(base_url + "/productsList")
    # response = requests.get(f"{base_url}/productsList")
    assert response.status_code == 200
    assert len(response.json()["products"]) > 0

def test_create(base_url):
    response2 = requests.post(base_url + "/productsList")
    assert response2.json()["responseCode"] == 405
    assert response2.json()["message"] == "This request method is not supported."

def test_searchProduct(base_url):

    body = {
        "search_product": "jean"
    }
    res = requests.post(base_url + "/searchProduct",
                        data= body)
    
    assert res.status_code == 200
    print(res.json())
    # assert "jean" in res.json()["products"][0]["name"].lower() # lower() преобразует в нижний регистр

    list_products = res.json()["products"] # создаем список всех элементов
    print(list_products)

    for product in list_products:
        assert "jean" in product["name"].lower()

def test_search_product_without_parameter(base_url):
    res = requests.post(base_url + "/searchProduct")
    assert res.json()["responseCode"] == 400
    assert res.json()["message"] == "Bad request, search_product parameter is missing in POST request."

def test_login_with_valid_details(base_url):
    
    data = {
        "email": "olgaolga@rodchanka.by",
        "password": "AK6Hy@zAZMCdnUs"
    }
    # res = requests.post(base_url + "/verifyLogin",
    #                     data=data)
    
    # assert res.json()["responseCode"] == 200
    # assert res.json()["message"] == "User exists!"

  
   
def test_login_with_invalid_details(base_url):

    data = {
        "email": "olga@rodchanka.by",
        "password": "AK6Hy@zAZMCdnU"
    }
    res = requests.post(base_url + "/verifyLogin",
                        data=data)
    
    assert res.json()["responseCode"] == 404
    assert res.json()["message"] == "User not found!"

def test_create_user_account(base_url):

    new_email = f"test{time.time()}@gmail.com" # создание всегда нового пользователя
    data = {
        "name":"Olga",
        "email":new_email,
        "password":"123456789",
        "title":"Mrs",
        "birth_date":"06",
        "birth_month":"02",
        "birth_year":"1990",
        "firstname":"Olga",
        "lastname":"Rodchenko",
        "company":"company",
        "address1":"address1",
        "address2,":"address1",
        "country":"country1",
        "zipcode":"zipcode1",
        "state":"state1",
        "city":"city1",
        "mobile_number":"80295811515"
    }
    res = requests.post(base_url + "/createAccount",
                             data= data)
    print(res.json())
    assert res.json()["responseCode"] == 201
    assert res.json()["message"] == "User created!"

# def test_delete_user_account(base_url):
#     data = {
#         "email": "olgaolga@rodchanka.by",
#         "password": "AK6Hy@zAZMCdnUs"
#     }
#     res = requests.delete(base_url + "/deleteAccount",
#                         data=data)
    
#     assert res.json()["responseCode"] == 200
#     assert res.json()["message"] == "Account deleted!"


def test_update_user_account(base_url):
    data = {
        "name":"Masha",
        "email":"olar@mail.ru",
        "password":"123456789",
        "title":"Mrs",
        "birth_date":"06",
        "birth_month":"02",
        "birth_year":"1990",
        "firstname":"Olga",
        "lastname":"Rodchenko",
        "company":"company",
        "address1":"address1",
        "address2,":"address1",
        "country":"country1",
        "zipcode":"zipcode1",
        "state":"state1",
        "city":"city1",
        "mobile_number":"80295811515"

    }
    res = requests.put(base_url + "/updateAccount",
                           data= data)
    
    assert res.json()["responseCode"] == 200
    assert res.json()["message"] == "User updated!"

def test_user_account_detail_by_email(base_url):

    data = {
        "email":"olar@mail.ru"
    }
    res = requests.get(base_url + "/getUserDetailByEmail",
                       data= data)
    print(res.json())

    # assert res.json()["responseCode"] == 200
    # assert res.json()["message"] == "User Detail"