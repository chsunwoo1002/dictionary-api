import pytest
from app import app
from modules.utils import *

@pytest.fixture(scope='module')
def client():
    with app.test_client() as tester:
        yield tester

def testAppHome(client):
  response = client.get('/')
  assert response.status_code == 200
  assert response.data.decode("utf-8") == welcomeMessage

def testAppUsage(client):
  response = client.get('/usage')
  assert response.status_code == 200
  assert response.data.decode("utf-8") == usageMessage