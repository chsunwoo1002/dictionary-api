import pytest
from app import app
from modules.utils import *

@pytest.fixture(scope='module')
def tester():
    with app.test_client() as t:
        yield t

# Testing access to non-existing URL
def testPageNotFoundError(tester):
  response = tester.get('/errornotfound')
  assert response.status_code == 404
  assert response.data.decode('utf-8') == pageNotFoundErrorMessage

# Testing not allowed method (POST)
def testNotAllowedError(tester):
  reponse = tester.post('/', data= 'POST method')
  assert reponse.status_code == 405
  assert reponse.data.decode('utf-8') == notAllowedErrorMessage

# Testing missing word parameters
def testMissingWordParameters(tester):
  response = tester.get('/dictionary-api/v1/?word=&language=en-US')
  assert response.status_code == 422
  assert response.data.decode('utf-8') == unprocessableEntityMessage

# Testing missing language parameters
def testMissingLanguageParameters(tester):
  response = tester.get('/dictionary-api/v1/?word=apple&language=')
  assert response.status_code == 422
  assert response.data.decode('utf-8') == unprocessableEntityMessage

# Testing an invalid extra parameter
def testBadRequest(tester):
  response = tester.get('/dictionary-api/v1/?word=apple&language=en-US&extra=parameter')
  assert response.status_code == 400
  assert response.data.decode('utf-8') == badRequestErrorMessage