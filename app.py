from curses.ascii import HT
from distutils.debug import DEBUG
from flask import request, jsonify, Flask
from modules.googleDictionary import queryWord
from modules.utils import *
from werkzeug.exceptions import HTTPException, UnprocessableEntity, BadRequest

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

# Return JSON instead of HTML for HTTP errors.  
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

@app.route('/dictionary-api/v1/', methods=['GET'])
def apiSearch():
  # check length of parameters is correct
  if len(request.args) != 2:
    raise BadRequest

  # Check if an search was provided as part of the URL.
  # If search is provided, assign it to a variable.
  # If no search is provided, display an error in the browser.
  if 'word' in request.args and request.args['word'] != '':
    searchWord = request.args['word']
  else:
    raise UnprocessableEntity

  # Check if an language was provided as part of the URL.
  # If language is provided, assign it to a variable.
  # If no language is provided, display an error in the browser.
  if 'language' in request.args and request.args['language'] != '':
    language = request.args['language']
  else:
    raise UnprocessableEntity
    
  # get JSON which is about searching word
  # If it successfully finds, it returns "data" in type key
  # If it does not successfully find, it returns "error" in type key
  result = queryWord(searchWord, language)

  # Use the jsonify function from Flask to convert our list of
  # Python dictionaries to the JSON format.
  return jsonify(result)

if __name__ == "__main__":
    app.run()