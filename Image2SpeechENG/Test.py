import Config
import Utilities
from TesseractWrapper import TesseractWrapper
import Davinci_API
import os
import time

class TestOCR:
    def __init__(self, data):
        self.data = data
        self.ocr = TesseractWrapper()

    def test(self):
        request_count = 0
        wer = list()
        cer = list()
        wer_ocr = list()
        cer_ocr = list()
        for image, text in self.data:
            ocr_output = self.ocr.processImage(image)
            ocr_output = Utilities.remove_empty_lines(ocr_output)
            ocr_sentences = Utilities.split_text_into_sentences(ocr_output)
            corrected_sentences = list()
            for sentence in ocr_sentences:
                print("request_count: ", request_count)
                if request_count == 60:
                    time.sleep(10)
                    request_count = 0
                gpt_out = Davinci_API.correct_sentence(sentence)
                request_count+=1
                corrected_sentences.append(gpt_out)
            gt = Utilities.read_file(text)
            tmp_wer = Utilities.WER(' '.join(gt), ' '.join(corrected_sentences))
            tmp_cer = Utilities.CER(' '.join(gt), ' '.join(corrected_sentences))
            tmp_wer_ocr = Utilities.WER(' '.join(gt), ocr_output)
            tmp_cer_ocr = Utilities.CER(' '.join(gt), ocr_output)
            print("tmp_wer: ", tmp_wer)
            print("tmp_cer: ", tmp_cer)
            print("tmp_wer_ocr: ", tmp_wer_ocr)
            print("tmp_cer_ocr: ", tmp_cer_ocr)
            wer.append(tmp_wer)
            cer.append(tmp_cer)
            wer_ocr.append(tmp_wer_ocr)
            cer_ocr.append(tmp_cer_ocr)
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ["Ground truth:"])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), gt)
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['\n'])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['OCR:'])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), [ocr_output])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['\n'])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['Corrected:'])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), corrected_sentences)
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['\n'])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['WER (gt vs final): ' + str(tmp_wer)])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['CER (gt vs final): ' + str(tmp_cer)])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['WER% (gt vs final): ' + str(100 * tmp_wer)])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['CER% (gt vs final): ' + str(100 * tmp_cer)])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['\n'])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['WER (gt vs ocr): ' + str(tmp_wer_ocr)])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['CER (gt vs ocr): ' + str(tmp_cer_ocr)])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['WER (gt vs ocr): ' + str(100 * tmp_wer_ocr)])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['CER (gt vs ocr): ' + str(100 * tmp_cer_ocr)])
        average_wer = sum(wer) / len(wer)
        average_cer = sum(cer) / len(cer)
        average_wer_ocr = sum(wer) / len(wer)
        average_cer_ocr = sum(cer) / len(cer)
        return (average_wer, average_cer, average_wer_ocr, average_cer_ocr)

def getImageTextPairs(image_path, text_path):
    images = os.listdir(image_path)
    texts = os.listdir(text_path)
    assert len(images) == len(texts)
    imageTextPairList = list()
    for i in range(len(images)):
        imageTextPairList.append((image_path + '/' + images[i], text_path + '/' + texts[i]))
    return imageTextPairList

if __name__ == '__main__':
    data = getImageTextPairs(Config.testImagesDir, Config.testTextsDir)
    test = TestOCR(data)
    results = test.test()
    print(results)
    Utilities.write_file(Config.tmpDir + '/' + "average.txt", ["WER CER WER_OCR CER_OCR"])
    Utilities.write_file(Config.tmpDir + '/' + "average.txt", results)