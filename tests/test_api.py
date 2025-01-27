import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_incident_route(client):
    response = client.get('/api/incidents')
    assert response.status_code == 200



#test the git