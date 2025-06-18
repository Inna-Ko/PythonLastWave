import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


class TestRestAPI:

    @pytest.mark.parametrize("post_id,expected_status", [
        (1, 200),
        (100, 200),
        (101, 404),
        (0, 404),
        (-1, 404),
        ("abc", 404),
    ])
    def test_get_post_by_id(self, post_id, expected_status):
        url = f"{BASE_URL}/posts/{post_id}"
        response = requests.get(url)

        assert response.status_code == expected_status

        if expected_status == 200:
            data = response.json()
            assert "id" in data
            assert "title" in data
            assert "body" in data
            assert "userId" in data
            assert data["id"] == post_id

    def test_get_all_posts(self):
        url = f"{BASE_URL}/posts"
        response = requests.get(url)

        assert response.status_code == 200
        data = response.json()
        assert len(data) == 100
        assert isinstance(data, list)

    @pytest.mark.parametrize("post_data,expected_status", [
        ({
             "title": "Test Post",
             "body": "This is a test post",
             "userId": 1
         }, 201),
        ({
             "title": "Another Test",
             "body": "Another test post with different content",
             "userId": 2
         }, 201)
    ])
    def test_create_post(self, post_data, expected_status):
        url = f"{BASE_URL}/posts"
        response = requests.post(url, json=post_data)

        assert response.status_code == expected_status

        if expected_status == 201:
            data = response.json()
            assert "id" in data
            assert data["title"] == post_data["title"]
            assert data["body"] == post_data["body"]
            assert data["userId"] == post_data["userId"]
            assert data["id"] == 101

    @pytest.mark.parametrize("post_id,update_data,expected_status", [
        (1, {
            "id": 1,
            "title": "Updated Title",
            "body": "Updated body content",
            "userId": 1
        }, 200),
        (50, {
            "id": 50,
            "title": "Another Update",
            "body": "Another updated content",
            "userId": 2
        }, 200),
        (1, {
            "title": "Only Title Updated"
        }, 200)
    ])
    def test_update_post_put(self, post_id, update_data, expected_status):
        url = f"{BASE_URL}/posts/{post_id}"
        response = requests.put(url, json=update_data)

        assert response.status_code == expected_status

        if expected_status == 200:
            data = response.json()
            assert data["id"] == post_id
            for key, value in update_data.items():
                if key in data:
                    assert data[key] == value

    @pytest.mark.parametrize("post_id,expected_status", [
        (3, 200),
        (50, 200),
        (100, 200),
    ])
    def test_delete_post(self, post_id, expected_status):
        url = f"{BASE_URL}/posts/{post_id}"
        response = requests.delete(url)

        assert response.status_code == expected_status
