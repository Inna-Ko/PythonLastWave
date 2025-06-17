import pytest
import requests


class TestPages:

    @pytest.mark.parametrize("domain", open("domains.txt").readlines())
    def test_domain(self, domain):
        url = f"{domain.strip()}"
        response = requests.get(url)
        assert response.status_code == 200