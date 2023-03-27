import nltk
import Levenshtein

nltk.download('punkt')

def split_text_into_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

def read_file(file):
    with open(file, 'r') as file:
        # read the file into a list of lines
        lines = file.readlines()
        # remove newline characters from each line
        return [line.strip() for line in lines]

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

def cer(gt, pred):
    """
    Calculates the Character Error Rate (CER) between two strings.
    :param gt: Ground truth string
    :param pred: Predicted string
    :return: CER value
    """
    # Remove whitespaces and convert to lowercase
    gt = gt.strip().lower()
    pred = pred.strip().lower()
    # Calculate Levenshtein distance between the two strings
    lev_distance = Levenshtein.distance(gt, pred)
    # Calculate CER
    cer = lev_distance / max(len(gt), 1)
    return cer
