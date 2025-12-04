# pylint: disable=redefined-outer-name
"""
Testing gists api calls for non-existent-user, octocat and root api calls
"""
import pytest
from fastapi.testclient import TestClient
from app import app

@pytest.fixture
def test_client():
    """
    initiate client
    """
    return TestClient(app)


def test_octocat_gists(test_client):
    """
    collecting the octocat gists and verifying the responses
    """
    response = test_client.get('/octocat')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'id' in data[0]
    assert 'description' in data[0]
    assert 'url' in data[0]
    assert 'files' in data[0]


def test_nonexistent_user(test_client):
    """
    Verifying the responses for the non existent user
    """
    response = test_client.get('/thisuserdoesnotexist123456789')
    assert response.status_code == 404
    data = response.json()
    assert 'detail' in data


def test_root(test_client):
    """
    verifying the response for the root api call
    """
    response = test_client.get('/')
    assert response.status_code == 200
    data = response.json()
    assert 'message' in data
    assert 'usage' in data


def test_health(test_client):
    """
    Verifying the status api call
    """
    response = test_client.get('/health')
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'healthy'
