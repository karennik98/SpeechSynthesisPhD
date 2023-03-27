import nltk
import Config

nltk.download('punkt')

def Text2Sentences(text):
    return nltk.sent_tokenize(text)

def FilterSentencesWithLen(sentences):
    filteredSentences = list()
    for sent in sentences:
        if len(sent) <= Config.maxAllowedSentenceLen:
            filteredSentences.append(sent)
    return filteredSentences

def CleanSentences(sentences):
    return [sent.replace('<br /><br />', '') for sent in sentences]