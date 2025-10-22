import pytest
from fastapi.testclient import TestClient
from app import app

@pytest.fixture
def client():
    return TestClient(app)

def test_octocat_gists(client):
    response = client.get('/octocat')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'id' in data[0]
    assert 'description' in data[0]
    assert 'url' in data[0]
    assert 'files' in data[0]

def test_nonexistent_user(client):
    response = client.get('/thisuserdoesnotexist123456789')
    assert response.status_code == 404
    data = response.json()
    assert 'detail' in data

def test_root(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.json()
    assert 'message' in data
    assert 'usage' in data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'healthy'