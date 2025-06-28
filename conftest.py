import pytest
import requests


@pytest.fixture
def get_joke():
    response = requests.get("https://geek-jokes.sameerkumar.website/api")
    return response.text
