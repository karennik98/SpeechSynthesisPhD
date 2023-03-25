from TesseractWrapper import TesseractWrapper
import Utilities
import PyTTS
import GPT_API

if __name__ == '__main__':
    ocr_model = TesseractWrapper()
    ocr_output = ocr_model.processImage("C:\\Users\\karen\\PhD\\SpellCorrectorENG\\Assets\\TestImages\\A_Book_of_Escapes_and_Hurried_Journeys.pdf.jpg")

    sentences = Utilities.split_text_into_sentences(ocr_output)
    print("len: ", len(sentences))

    corrected_sentences = list()
    for sentence in sentences:
        gpt_out = GPT_API.correct_sentence(sentence)
        corrected_sentences.append(gpt_out)

    print("len of corrected_sentences: ", len(corrected_sentences))
    speech = " ".join(corrected_sentences)
    PyTTS.textToSpeech(speech)



