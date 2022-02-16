import json

# json variables for app
welcomeMessage = json.dumps({'message':'Welcome to Dictionary API with google crawling'})
usageMessage = json.dumps(
  {
    'message': 'Basic usage of API', 
    'endPoints': {
      '/' : 'root URL with welcoming message',
      '/dictionary-api/v1/' : 'end points for searching word',
      'usage' : 'end point for seeing usage'
   },
    'example' : 'https://dictionary-api-flask.herokuapp.com/dictionary-api/v1/word=apple&language=en-US',
    'supportedLanguage' : ['en-Us']
  })
pageNotFoundErrorMessage = json.dumps(
  {
   'code': 404, 
   'name': 'Not Found', 
   'description': 'The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'
  }
)
notAllowedErrorMessage = json.dumps(
  {
    "code": 405, 
    "name": "Method Not Allowed", 
    "description": "The method is not allowed for the requested URL."
  }
)
badRequestErrorMessage = json.dumps(
  {
    'code' : 400,
    'detail' : '''server is unable to process the request sent by the client.'''
  }
)

unprocessableEntityMessage = json.dumps(
  {
    'code' : 422,
    'detail' : '''server is unable to process the contained instructions. Please check parameters.'''
  }
)

# variables for crawling 
callback, payload, results, entry = 'feature-callback', 'payload', 'single_results', 'entry'
headword, phonetics, senseFamilies = 'headword', 'phonetics', 'sense_families'
text, oxfordAudio = 'text', 'oxford_audio'
partsOfSpeech, value, senses = 'parts_of_speech', 'value', 'senses'
definition, examples, exampleGroups, additionalExamples, thesaurusEntries, antonyms, synonyms,nym, nyms = 'definition','examples','example_groups','additional_examples','thesaurus_entries','antonyms','synonyms','nym', 'nyms'
