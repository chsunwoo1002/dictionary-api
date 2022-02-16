from distutils.debug import DEBUG
import json
from flask import request, jsonify, Flask
from modules.googleDictionary import queryWord
from modules.utils import *

app = Flask(__name__)
app.config.from_mapping(
  DEBUG=True,
  TESTING=True,
)

@app.route('/', methods=['GET'])
def home():
  return welcomeMessage

@app.route('/usage', methods=['GET'])
def usage():
  return usageMessage

@app.errorhandler(400)
def badRequest():
  return pageNotFoundErrorMessage, 400

@app.errorhandler(404)
def pageNotFound():
  return badRequestErrorMessage, 404

@app.errorhandler(422)
def unprocessableEntity():
  return unprocessableEntityMessage, 422

@app.route('/dictionary-api/v1/', methods=['GET'])
def apiSearch():
  # Check if an search was provided as part of the URL.
  # If search is provided, assign it to a variable.
  # If no search is provided, display an error in the browser.
  if 'word' in request.args:
    searchWord = request.args['word']
  else:
    raise unprocessableEntity()

  # Check if an language was provided as part of the URL.
  # If language is provided, assign it to a variable.
  # If no language is provided, display an error in the browser.
  if 'language' in request.args:
    language = request.args['language']
  else:
    return unprocessableEntity()

  # get JSON which is about searching word
  # If it successfully finds, it returns "data" in type key
  # If it does not successfully find, it returns "error" in type key
  result = queryWord(searchWord, language)

  # Use the jsonify function from Flask to convert our list of
  # Python dictionaries to the JSON format.
  return jsonify(result)

if __name__ == "__main__":
    app.run()