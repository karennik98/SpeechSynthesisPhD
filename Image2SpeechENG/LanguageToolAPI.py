import requests
import json

def correct_text(text):
    # Set the LanguageTool API endpoint and parameters
    endpoint = 'https://api.languagetool.org/v2/check'
    params = {
        'text': text,  # Input text to check
        'language': 'en-US',  # Language code for English (US)
        'disabledRules': 'WHITESPACE_RULE',  # Optional parameter to disable specific rules
    }

    # Send a request to the API and parse the response
    response = requests.get(endpoint, params=params)
    result = json.loads(response.text)

    # Extract and concatenate the corrected text from the API response
    matches = result['matches']
    corrected_text = ""
    last_index = 0
    for match in matches:
        corrected_text += text[last_index:match['offset']] + match['replacements'][0]['value']
        last_index = match['offset'] + match['length']
    corrected_text += text[last_index:]

    return corrected_text
