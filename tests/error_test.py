import pytest
from app import app
from modules.utils import *

@pytest.fixture(scope='module')
def client():
    with app.test_client() as tester:
        yield tester

def testPageNotFoundError(client):
  response = client.get('/errornotfound')
  assert response.status_code == 404
  assert response.data.decode('utf-8') == pageNotFoundErrorMessage

def testNotAllowedError(client):
  reponse = client.post('/', data= 'POST method')
  assert reponse.status_code == 405
  assert reponse.data.decode('utf-8') == notAllowedErrorMessage

# def testBadRequestError(cleint):
# def testUnprocessableEntityError(client):
