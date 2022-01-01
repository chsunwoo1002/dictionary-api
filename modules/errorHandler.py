def pageNotFoundError():
  errorMessage = {}
  errorMessage["type"] = "error"
  errorMessage["infomation"] = "The page is not Found"
  return errorMessage

def serverError():
  errorMessage = {}
  errorMessage["type"] = "server"
  errorMessage["infomation"] = "The sever error occurs"
  return errorMessage

def connectionError():
  errorMessage = {}
  errorMessage["type"] = "server"
  errorMessage["infomation"] = "connection error occurs, please try it later"
  return errorMessage

def HTTPError():
  errorMessage = {}
  errorMessage["type"] = "server"
  errorMessage["infomation"] = "HTTP error occurs, please try it later"
  return errorMessage