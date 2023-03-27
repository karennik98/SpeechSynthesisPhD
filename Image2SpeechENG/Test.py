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
        for image, text in self.data:
            ocr_output = self.ocr.processImage(image)
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
            print("tmp_wer: ", tmp_wer)
            print("tmp_cer: ", tmp_cer)
            wer.append(tmp_wer)
            cer.append(tmp_cer)
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ["Ground truth:"])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), gt)
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['\n'])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['Corrected:'])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), corrected_sentences)
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['\n'])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['WER: ' + str(tmp_wer)])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['CER: ' + str(tmp_cer)])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['WER%: ' + str(100 * tmp_wer)])
            Utilities.write_file(Config.tmpDir + '/' + os.path.basename(text), ['CER%: ' + str(100 * tmp_cer)])
        average_wer = sum(wer) / len(wer)
        average_cer = sum(cer) / len(cer)
        return (average_wer, average_cer)

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