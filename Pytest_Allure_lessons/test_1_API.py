import time

import requests
from seleniumwire import webdriver


class TestJsonPlaceholder: # Название тестового класса

    def test_get_jsonplaceholder(self):
        response = requests.get("https://jsonplaceholder.typicode.com/")
        assert response.status_code == 200, "Некорректный ответ от сервера"

    def test_get_responses(self):
        driver = webdriver.Chrome()
        driver.get("https://jsonplaceholder.typicode.com/")
        time.sleep(7)
        for request in driver.requests:
            if request.response:
                print(request.method, request.url, request.response.status_code)
                assert request.response.status_code == 200, f"Некорректный ответ от сервера в запросе {request.url}"
