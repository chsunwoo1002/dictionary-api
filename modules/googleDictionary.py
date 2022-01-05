import requests
import json
import modules.errorHandler as errorHandler

# put variables in utils.py
callback, payload, results, entry = "feature-callback", "payload", "single_results", "entry"
headword, phonetics, senseFamilies = "headword", "phonetics", "sense_families"
text, oxfordAudio = "text", "oxford_audio"
partsOfSpeech, value, senses = "parts_of_speech", "value", "senses"
definition, examples, exampleGroups, additionalExamples, thesaurusEntries, antonyms, synonyms,nym, nyms = "definition","examples","example_groups","additional_examples","thesaurus_entries","antonyms","synonyms","nym", "nyms"

def queryWord(word, language):
  # header shall be implemented
  key = {
    "fc": "EswBCowBQU1sdnJwdTI0em0tQ2E2aVBzSWJ0T0s5ckUwT2MwbVdYMzJjNkgxSXU0bzcwQUVvZnZyLXpHSzBpWGxjMU9SVEtXaEptaXZjQ3JBaHAzeURLSVoyMGtVR1VGaU9JQUx6ZXlRY0NfYVhBbmpzZ2ZIcXZrT045YUJVNnVQdFBndDdac2NaTG1vMjcyU3MSF0lSRE9ZWWlhRmVySjBQRVAtTDJpNkE4GiJBSFdTTm1YRFQtQnBvbFkxSkxZV1ljTHNfWk5yTjlrT3BR",
    "fcv" : "3",
    "async" : f"term:{word},corpus:{language},hhdr:true,hwdgt:true,wfp:true,ttl:,tsl:,ptl:"

  }
  try:
    response = requests.get("https://www.google.com/async/callback:5493", params=key)
  except requests.HTTPError:
    return errorHandler.HTTPError()
  except requests.ConnectionError:
    return errorHandler.connectionError()
  else:
    if response.status_code == 200:
      return parseData(json.loads(response.text[4:])[callback][payload][results][0][entry])
    if response.status_code == 500: # server error
      return errorHandler.serverError()
    if response.status_code == 404: # page not found error
      return errorHandler.pageNotFoundError()
    return 0

def findWord(word, language):
  data = queryWord(word, language)
  
  return parseData(data)

def parseData(data):
  dictionaryData = {}
  dictionaryData["type"] = "data"
  dictionaryData["word"] = data[headword]
  dictionaryData["phonetics"] = list(map(getPhonetics, data[phonetics]))
  dictionaryData["meaning"] = list(map(getMeaning, data[senseFamilies]))
  
  return dictionaryData

def getPhonetics(phoneticData):
  result = {}
  result["text"] = phoneticData[text]
  if "oxford_audio" in phoneticData:
    result["audio"] = phoneticData[oxfordAudio]
  
  return result

def getMeaning(meaningData):
  result = {}
  result["partOfSpeech"] = meaningData[partsOfSpeech][0][value]
  result["definitions"] = list(map(getDefinitions, meaningData[senses]))
    
  return result

def getDefinitions(definitionData):
  result = {}
  result["definition"] = definitionData[definition][text]
  result["examples"] = []
  if exampleGroups in definitionData:
    result["examples"] = list(map(lambda example: example[examples][0], definitionData[exampleGroups]))
  if additionalExamples in definitionData:
    result["examples"].extend(definitionData[additionalExamples])
  if thesaurusEntries in definitionData:
    if antonyms in definitionData[thesaurusEntries][0]:
      result["antonyms"] = list(map(lambda antonym: antonym[nym], definitionData[thesaurusEntries][0][antonyms][0][nyms]))
    if synonyms in definitionData[thesaurusEntries][0]:
      result["synonyms"] = list(map(lambda antonym: antonym[nym], definitionData[thesaurusEntries][0][synonyms][0][nyms]))
  
  return result
