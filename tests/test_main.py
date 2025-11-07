from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello CI/CD"}


def test_read_2_root():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world"}


def test_hola_endpoint():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "test endpoint"}
