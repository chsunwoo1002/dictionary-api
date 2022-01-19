# Error handler modules

def pageNotFoundError():
  errorMessage = {}
  errorMessage["type"] = "error"
  errorMessage["infomation"] = '''The page is not Found
  please check the correctness of searching word'''
  return errorMessage

def serverError():
  errorMessage = {}
  errorMessage["type"] = "error"
  errorMessage["infomation"] = '''The sever error occurs
  Please check the correctness of searching word'''
  return errorMessage

def connectionError():
  errorMessage = {}
  errorMessage["type"] = "error"
  errorMessage["infomation"] = "connection error occurs, please try it later"
  return errorMessage

def HTTPError():
  errorMessage = {}
  errorMessage["type"] = "error"
  errorMessage["infomation"] = "HTTP error occurs, please try it later"
  return errorMessage