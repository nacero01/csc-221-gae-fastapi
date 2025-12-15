from fastapi.testclient import TestClient
from .main import app
import os

client = TestClient(app)


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "hello"

def test_my_empl_id():
    response = client.get("/id")
    assert response.status_code == 200
    assert response.json()['empl_id'] == '23759741'
