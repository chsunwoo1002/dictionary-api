from distutils.debug import DEBUG
from flask import request, jsonify, Flask
from modules.googleDictionary import queryWord

app = Flask(__name__)
app.config.from_mapping(
  DEBUG=True,
  TESTING=True,
)


@app.route('/', methods=['GET'])
def home():
  return '<h1>Dictionary API with google crawling</h1>'

@app.route('/usage', method=['GET'])
def usage():
  return '<h1>Usage:/word=word&language=en-US</h1>'

@app.errorhandler(400)
def badRequest(e):
  return "<h1>400</h1><p>The resource could not be found.</p>", 400

@app.errorhandler(404)
def pageNotFound(e):
  return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/dictionary-api/v1/', methods=['GET'])
def apiSearch():
  # Check if an search was provided as part of the URL.
  # If search is provided, assign it to a variable.
  # If no search is provided, display an error in the browser.
  if 'word' in request.args:
    searchWord = request.args['word']
  else:
    return "Error: No word field provided. Please specify an searching word."

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

if __name__ == "__main__":
    app.run(debug=True)