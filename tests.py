# 14f022d092643cb7f77eb0e7c70661b8

# https://home.openweathermap.org/api_keys

import pytest
import requests
from dotenv import load_dotenv
import os

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")



API_KEY = '131ba58c898e27a8ea373e96ce0cc470'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


@pytest.fixture
def api_key():
    return API_KEY


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.mark.parametrize("city", ["London", "New York", "Tokyo"])
def test_valid_city(api_key, base_url, city):
    response = requests.get(f"{base_url}?q={city}&appid={api_key}")
    assert response.status_code == 200
    assert 'main' in response.json()


def test_missing_api_key(base_url):
    response = requests.get(f"{base_url}?q=London")
    assert response.status_code == 401


def test_missing_city(base_url, api_key):
    response = requests.get(f"{base_url}?appid={api_key}")
    assert response.status_code == 400


def test_invalid_api_key(base_url):
    response = requests.get(f"{base_url}?q=London&appid=invalidkey")
    assert response.status_code == 401


def test_valid_city_and_country(api_key, base_url):
    response = requests.get(f"{base_url}?q=London,uk&appid={api_key}")
    assert response.status_code == 200
    assert 'main' in response.json()


def test_valid_zip_code(api_key, base_url):
    response = requests.get(f"{base_url}?zip=10001,us&appid={api_key}")
    assert response.status_code == 200
    assert 'main' in response.json()


def test_invalid_zip_code(api_key, base_url):
    response = requests.get(f"{base_url}?zip=00000,us&appid={api_key}")
    assert response.status_code == 404


def test_valid_coordinates(api_key, base_url):
    response = requests.get(f"{base_url}?lat=35&lon=139&appid={api_key}")
    assert response.status_code == 200
    assert 'main' in response.json()


def test_valid_city_and_state(api_key, base_url):
    response = requests.get(f"{base_url}?q=New York,us&appid={api_key}")
    assert response.status_code == 200
    assert 'main' in response.json()


def test_invalid_city_and_state(api_key, base_url):
    response = requests.get(f"{base_url}?q=NonExistingCity,NonExistingState&appid={api_key}")
    assert response.status_code == 404


def test_valid_language(api_key, base_url):
    response = requests.get(f"{base_url}?q=Tokyo&lang=ja&appid={api_key}")
    assert response.status_code == 200
    assert 'main' in response.json()


def test_valid_city_and_state_code(api_key, base_url):
    response = requests.get(f"{base_url}?q=Los Angeles,US&appid={api_key}")
    assert response.status_code == 200
    assert 'main' in response.json()


def test_invalid_city_and_state_code(api_key, base_url):
    response = requests.get(f"{base_url}?q=NonExistingCity,XY&appid={api_key}")
    assert response.status_code == 404


def test_valid_city_and_country_code(api_key, base_url):
    response = requests.get(f"{base_url}?q=Berlin,DE&appid={api_key}")
    assert response.status_code == 200
    assert 'main' in response.json()


def test_invalid_city_and_country_code(api_key, base_url):
    response = requests.get(f"{base_url}?q=NonExistingCity,XX&appid={api_key}")
    assert response.status_code == 404