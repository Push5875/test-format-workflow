import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.json == {"message": "Welcome to the API!"}

def test_echo(client):
    rv = client.get('/about')
    assert rv.status_code == 200
    assert rv.json == {"version": "1.0", "author": "Yagmur Ozden"}
