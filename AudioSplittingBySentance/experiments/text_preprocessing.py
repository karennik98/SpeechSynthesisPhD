import Config
import TextUtilities


def preprocess(file_path):
    text = TextUtilities.read_docx_file(file_path)
    print("Before preprocessing")
    print(text)

    print("After preprocessing")
    for char in Config.characters2remove:
        text = text.replace(char, '')
    print(text)


if __name__ == "__main__":
    preprocess("C:\\Users\\karenn\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\input\\hopopy\\hopop.docx")
