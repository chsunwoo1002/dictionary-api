import flask
from flask import request, jsonify, Flask
from modules.googleDictionary import queryWord

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Google Dictionary API</h1>
<p>A prototype API for distant words</p>'''

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/searches', methods=['GET'])
def api_search():
  # Check if an ID was provided as part of the URL.
  # If ID is provided, assign it to a variable.
  # If no ID is provided, display an error in the browser.
  if 'search' in request.args:
    searchWord = request.args['search']
  else:
    return "Error: No search field provided. Please specify an searching word."

  if 'language' in request.args:
    language = request.args['language']
  else:
    return "Error: No language field provided. Please specify an searching language."
  # Loop through the data and match results that fit the requested ID.
  # IDs are unique, but other fields might return many results
  result = queryWord(searchWord, language)

  # Use the jsonify function from Flask to convert our list of
  # Python dictionaries to the JSON format.
  return jsonify(result)

app.run()