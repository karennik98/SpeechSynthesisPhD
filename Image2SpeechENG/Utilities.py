import nltk
from jiwer import wer
from jiwer import cer

nltk.download('punkt')

def split_text_into_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

def read_file(file):
    with open(file, 'r') as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

def write_file(file_name, sentences):
    with open(file_name, "a") as f:
        for item in sentences:
            f.write(item + "\n")

def WER(reference, hypothesis):
    if len(reference) == 0 or len(hypothesis) == 0:
        return 1.0
    return wer(reference, hypothesis)

def CER(gt, pred):
    if len(gt) == 0 or len(pred) == 0:
        return 1.0
    return cer(gt, pred)
