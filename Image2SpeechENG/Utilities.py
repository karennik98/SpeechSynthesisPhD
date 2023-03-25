import nltk
import re
import Levenshtein

nltk.download('punkt') # download the required tokenizer data

def split_text_into_sentences(text):
    sentences = nltk.sent_tokenize(text)
    # sentences = re.split(r'[.!?]+', text)
    return sentences

def wer(reference, hypothesis):
    """
    Calculate the Word Error Rate (WER) metric between the reference and hypothesis strings
    """
    # Split reference and hypothesis into words
    ref_words = reference.split()
    hyp_words = hypothesis.split()

    # Calculate edit distance using Levenshtein distance algorithm
    distance = Levenshtein.distance(reference, hypothesis)

    # Calculate WER
    wer_result = distance / len(ref_words)

    return wer_result