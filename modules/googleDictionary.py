import requests
import json

callback, payload, results = "feature-callback","payload", "single_results"
def queryWord(word, language):
  # header shall be implemented
  key = {
    "fc": "EswBCowBQU1sdnJwdTI0em0tQ2E2aVBzSWJ0T0s5ckUwT2MwbVdYMzJjNkgxSXU0bzcwQUVvZnZyLXpHSzBpWGxjMU9SVEtXaEptaXZjQ3JBaHAzeURLSVoyMGtVR1VGaU9JQUx6ZXlRY0NfYVhBbmpzZ2ZIcXZrT045YUJVNnVQdFBndDdac2NaTG1vMjcyU3MSF0lSRE9ZWWlhRmVySjBQRVAtTDJpNkE4GiJBSFdTTm1YRFQtQnBvbFkxSkxZV1ljTHNfWk5yTjlrT3BR",
    "fcv" : "3",
    "async" : f"term:{word},corpus:{language},hhdr:true,hwdgt:true,wfp:true,ttl:,tsl:,ptl:"

  }
  response = requests.get("https://www.google.com/async/callback:5493", params=key, headers=headerObject)
  # error handler shall be implmented
  return json.loads(response.text[4:])

def findWord(word, language):
  wordObject = queryWord(word, language)
  return parseObject(wordObject)

def parseObject(obj):
  # filter object elements
  return obj
s = findWord("apple", "en-US")
print(s)
