# Google Crawler error handler modules
import json

crawlerPageNotFoundErrorMessage = json.dumps(
  {
   'code': 400, 
   'name': 'Not Found', 
   'description': 'The requested URL was not found on Google. Please check your spelling and try again.'
  }
)

crawlerInternalServerErrorMessage = json.dumps(
  {
   'code': 500, 
   'name': 'Internal Server Error', 
   'description': '''Something has gone wrong on the Google's server, but the server could not be more specific on what the exact problem is.'''
  }
)

crawlerUncaughtErrorMessage = json.dumps(
  {
    'name': 'uncaught Error',
    'description': 'The unkown error has been occured between server and Google. Please check your speeling and try again'
  }
)