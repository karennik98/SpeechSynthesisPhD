from spellchecker import SpellChecker
import re

def check_text(sentence):
    # define a custom regex pattern that matches all characters except whitespace
    pattern = re.compile(r"[^\s]+")

    # create a SpellChecker object
    spell = SpellChecker(language="en", case_sensitive=True)

    # tokenize the sentence using the custom regex pattern
    tokens = re.findall(pattern, sentence)

    # create a list to store the corrected words
    corrected_tokens = []

    # loop through the tokens and correct the spelling
    for token in tokens:
        # check if the token is misspelled
        if spell.correction(token) != token:
            # if the token is misspelled, replace it with the corrected spelling
            corrected_tokens.append(spell.correction(token))
        else:
            # if the token is spelled correctly, add it to the list of corrected tokens
            corrected_tokens.append(token)

    # join the corrected tokens into a sentence
    corrected_sentence = " ".join(corrected_tokens)

    return corrected_sentence