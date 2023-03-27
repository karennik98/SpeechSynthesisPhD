import Utilities
from TesseractWrapper import TesseractWrapper
import Davinci_API

class TestOCR:
    def __init__(self, data):
        self.data = data
        self.ocr = TesseractWrapper()

    def test(self):
        wer = list()
        cer = list()
        for image, text in self.data:
            ocr_output = self.ocr.processImage(image)
            ocr_sentences = Utilities.split_text_into_sentences(ocr_output)
            corrected_sentences = list()
            for sentence in ocr_sentences:
                gpt_out = Davinci_API.correct_sentence(sentence)
                corrected_sentences.append(gpt_out)
            gt = Utilities.read_file(text)
            tmp_wer = Utilities.wer(' '.join(gt), ' '.join(corrected_sentences))
            tmp_cer = Utilities.cer(' '.join(gt), ' '.join(corrected_sentences))
            wer.append(tmp_wer)
            cer.append(tmp_cer)
        average_wer = sum(wer) / len(wer)
        average_cer = sum(cer) / len(cer)
        return (average_wer, average_cer)


if __name__ == '__main__':
    pass