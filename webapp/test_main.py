from fastapi.testclient import TestClient
from webapp.main import app

# filepath: /workspaces/mslearn-copilot-codespaces-python/webapp/test_main.py

client = TestClient(app)


def test_get_cities_spain():
    response = client.get("/cities/Spain")
    assert response.status_code == 200
    assert response.json() == {"country": "Spain", "cities": []}
