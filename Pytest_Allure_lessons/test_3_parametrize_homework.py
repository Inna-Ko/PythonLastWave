import requests
import pytest


BASE_URL = "http://users.bugred.ru/tasks/rest"

@pytest.mark.parametrize("method_name, payload, expected_status", [
    ("dologin", {"username": "testuser", "password": "testpass"}, 200),
    ("createuser", {"name": "New User", "email": "newuser@example.com"}, 200),
    ("getuser", {"id": 1}, 200),
    ("createtask", {"title": "New Task", "description": "Task description"}, 200)
])
def test_api_methods(method_name, payload, expected_status):
    url = f"{BASE_URL}/{method_name}"
    response = requests.post(url, json=payload)
    assert response.status_code == expected_status


# Task 2

