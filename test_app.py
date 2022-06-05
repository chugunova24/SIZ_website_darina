from app import app, basedir
import pytest
import os

def test_home_page():
    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200


def test_connect_bd():
    pass


def test_exsist_dir():
    path = os.path.join(basedir, 'uploads')
    print(path)
    if len(os.listdir(path)) != 0:
        return True
    else:
        return False

test_exsist_dir()

