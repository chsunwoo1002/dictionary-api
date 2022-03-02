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

def argValidation(args):
  # check length of parameters is correct
  if len(args) != 2:
    raise BadRequest

  # Check if an search was provided as part of the URL.
  # If search is provided, assign it to a variable.
  # If no search is provided, display an error in the browser.
  if 'word' in args and args['word'] != '':
    searchWord = args['word']
  else:
    raise UnprocessableEntity

  # Check if an language was provided as part of the URL.
  # If language is provided, assign it to a variable.
  # If no language is provided, display an error in the browser.
  if 'language' in args and args['language'] != '':
    language = args['language']
  else:
    raise UnprocessableEntity
  
  return searchWord, language

@app.route('/dictionary-api/v1/synonyms/', methods=['GET'])
def synonymsSearch():
  searchWord, language = argValidation(request.args)
    
  # get JSON which is about searching word
  # If it successfully finds, it returns "data" in type key
  # If it does not successfully find, it returns "error" in type key
  word = queryWord(searchWord, language)
  result = getRelevantWords(word, syn, language)
  # Use the jsonify function from Flask to convert our list of
  # Python dictionaries to the JSON format.
  return result


@app.route('/dictionary-api/v1/word/', methods=['GET'])
def wordSearch():
  searchWord, language = argValidation(request.args)
    
  # get JSON which is about searching word
  # If it successfully finds, it returns "data" in type key
  # If it does not successfully find, it returns "error" in type key
  result = queryWord(searchWord, language)

  # Use the jsonify function from Flask to convert our list of
  # Python dictionaries to the JSON format.
  return result

if __name__ == "__main__":
    app.run()