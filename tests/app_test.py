import pytest
from app import app
from modules.utils import *
import json

@pytest.fixture(scope='module')
def client():
    with app.test_client() as tester:
        yield tester

# Testing welcome page
def testAppHome(client):
  response = client.get('/')
  assert response.status_code == 200
  assert response.data.decode("utf-8") == welcomeMessage

# Testing usage page
def testAppUsage(client):
  response = client.get('/usage')
  assert response.status_code == 200
  assert response.data.decode("utf-8") == usageMessage

# Testing valid API request
def testValidRequest(client):
  response = client.get('/dictionary-api/v1/?word=apple&language=en-US')
  assert response.status_code == 200
  data = json.loads(response.data.decode('utf-8'))
  assert "meaning" in data
  assert "word" in data
  assert "type" in data
  assert "phonetics" in data
  assert "definitions" in data["meaning"][0]
  assert "partOfSpeech" in data["meaning"][0]
  assert "definition" in data["meaning"][0]["definitions"][0]
  assert "examples" in data["meaning"][0]["definitions"][0]
  assert "text" in data["phonetics"][0]