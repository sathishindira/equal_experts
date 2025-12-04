"""
Testing gists api calls for non-existenet-user,octocat and root api calls
"""
import pytest
from fastapi.testclient import TestClient
from app import app

@pytest.fixture
def client():
    """
    initiate client
    """
    return TestClient(app)
    
cli_1 = client

def test_octocat_gists(cli_1):
    """
        collecting the octocat gists and verifing the responses
    """
    response = client.get('/octocat')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'id' in data[0]
    assert 'description' in data[0]
    assert 'url' in data[0]
    assert 'files' in data[0]

def test_nonexistent_user(cli_1):
    """
    Verifing the responses for the non existent user
    """
    response = client.get('/thisuserdoesnotexist123456789')
    assert response.status_code == 404
    data = response.json()
    assert 'detail' in data

def test_root(cli_1):
    """
    verifing the response for the root api call
    """
    response = client.get('/')
    assert response.status_code == 200
    data = response.json()
    assert 'message' in data
    assert 'usage' in data

def test_health(cli_1):
    """
    Verifing the status api call
    """
    response = client.get('/health')
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'healthy'

