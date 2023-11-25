import Config
import TextUtilities


def preprocess(text):
    for char in Config.characters2remove:
        text = text.replace(char, '')

    return text
