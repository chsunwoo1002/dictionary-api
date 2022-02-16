# Google Crawler error handler modules

def pageNotFoundError():
  errorMessage = {}
  errorMessage["type"] = "error"
  errorMessage["infomation"] = '''The Google page is not Found
  please check the correctness of searching word'''
  return errorMessage

def serverError():
  errorMessage = {}
  errorMessage["type"] = "error"
  errorMessage["infomation"] = '''The Google sever error occurs
  Please check the correctness of searching word'''
  return errorMessage

def connectionError():
  errorMessage = {}
  errorMessage["type"] = "error"
  errorMessage["infomation"] = "connection error with Google occurs, please try it later"
  return errorMessage

def HTTPError():
  errorMessage = {}
  errorMessage["type"] = "error"
  errorMessage["infomation"] = "HTTP error with Google occurs , please try it later"
  return errorMessage