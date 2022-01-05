import flask
from flask import request, jsonify, Flask
from modules.googleDictionary import queryWord

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Google Dictionary API</h1>
<p>A prototype API for distant words</p>
<p>Usage example:/api/v1/searches?search=apple&language=en-US </p>'''

@app.errorhandler(404)
def pageNotFound(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/searches', methods=['GET'])
def apiSearch():
  # Check if an search was provided as part of the URL.
  # If search is provided, assign it to a variable.
  # If no search is provided, display an error in the browser.
  if 'search' in request.args:
    searchWord = request.args['search']
  else:
    return "Error: No search field provided. Please specify an searching word."

  # Check if an language was provided as part of the URL.
  # If language is provided, assign it to a variable.
  # If no language is provided, display an error in the browser.
  if 'language' in request.args:
    language = request.args['language']
  else:
    return "Error: No language field provided. Please specify an searching language."

  # get JSON which is about searching word
  # If it successfully finds, it returns "data" in type key
  # If it does not successfully find, it returns "error" in type key
  result = queryWord(searchWord, language)

  # Use the jsonify function from Flask to convert our list of
  # Python dictionaries to the JSON format.
  return jsonify(result)

app.run()