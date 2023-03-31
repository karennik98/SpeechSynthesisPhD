import nltk
from jiwer import wer
from jiwer import cer
import pandas as pd
import Config

nltk.download('punkt')


def write_xlsx(wer_, cer_, wer_ocr, cer_ocr):
    average_wer = [sum(wer_) / len(wer_)]
    average_cer = [sum(cer_) / len(cer_)]
    average_wer_ocr = [sum(wer_ocr) / len(wer_ocr)]
    average_cer_ocr = [sum(cer_ocr) / len(cer_ocr)]

    max_length = max(len(wer_), len(cer_), len(wer_ocr), len(cer_ocr))
    wer_ += [None] * (max_length - len(wer_))
    cer_ += [None] * (max_length - len(cer_))
    wer_ocr += [None] * (max_length - len(wer_ocr))
    cer_ocr += [None] * (max_length - len(cer_ocr))
    average_wer += [None] * (max_length - len(average_wer))
    average_cer += [None] * (max_length - len(average_cer))
    average_wer_ocr += [None] * (max_length - len(average_wer_ocr))
    average_cer_ocr += [None] * (max_length - len(average_cer_ocr))

    df = pd.DataFrame({
        "WER (gt vs final)": wer_,
        "CER (gt vs final)": cer_,
        "WER (gt vs ocr)": wer_ocr,
        "CER (gt vs ocr)": cer_ocr,
        "Average WER(gt vs final)": average_wer,
        "Average CER(gt vs final)": average_cer,
        "Average WER(gt vs ocr)": average_wer_ocr,
        "Average CER(gt vs ocr)": average_cer_ocr})

    with pd.ExcelWriter(Config.tmpDir + '/' + 'metrics.xlsx') as writer:
        for i, column in enumerate(df.columns):
            df[[column]].to_excel(writer, sheet_name='Metrics', startcol=i, index=False)


def split_text_into_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return sentences


def remove_empty_lines(text):
    return '\n'.join(filter(lambda x: x.strip(), text.splitlines()))


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
