from get_data import get_json
import requests

# define a test function that tests the get_json function
# mock the response.get function using monkeypatch from pytest

def test_get_json(monkeypatch):
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code

        def json(self):
            return {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False}

    def mock_get(*args, **kwargs):
        return MockResponse(200)

    monkeypatch.setattr(requests, "get", mock_get)

    assert get_json("https://jsonplaceholder.typicode.com/todos/1") == {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False,
    }
    
# define a test function that tests the get_json function
# mock the response.get function using monkeypatch from pytest
# test that the function returns False

def test_get_json_false(monkeypatch):
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code

        def json(self):
            return {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False}

    def mock_get(*args, **kwargs):
        return MockResponse(404)

    monkeypatch.setattr(requests, "get", mock_get)

    assert get_json("https://jsonplaceholder.typicode.com/todos/1") == False