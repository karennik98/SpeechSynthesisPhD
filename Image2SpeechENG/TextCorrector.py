from spello.model import SpellCorrectionModel
import re
from pathlib import Path

def preprocess_train_data(train_data_path):
    with open(train_data_path, "r") as f:
        big = f.readlines()
    big  = [i.strip() for i in big]
    #Remove \t - tab
    big_t = [re.sub('\\t', ' ', text) for text in big]
    #Remove \\
    big_ = [re.sub("\\'", "", text) for text in big_t]
    #Remove
    big_r = [text for text in big_ if text != '']
    #Remove Special characters
    big_star = [re.sub(r'[^a-zA-Z]+', ' ', text) for text in big_r]
    print(big_star)
    #Remove leading and trailing spaces
    big_stripped = [text.strip() for text in big_star]
    return big_stripped


class TextCorrectionModel:
    def __init__(self):
        self.sp = SpellCorrectionModel(language='en')
        path = Path('C:\\Users\\karen\\PhD\\SpellCorrectorENG\\SpellCorrectionModel\\model.pkl')
        if path.is_file():
            self.model_path = "C:\\Users\\karen\\PhD\\SpellCorrectorENG\\SpellCorrectionModel\\model.pkl"
            self.sp.load(self.model_path)

    def train(self, train_data_path):
        big_stripped = preprocess_train_data(train_data_path)
        sp = SpellCorrectionModel(language='en')
        sp.train(big_stripped)
        model_path = sp.save("C:\\Users\\karen\\PhD\\SpellCorrectorENG\\SpellCorrectionModel")
        self.model_path = model_path
        print(model_path)

    def process(self, text):
        processed_text = self.sp.spell_correct(text)
        return processed_text['spell_corrected_text']

    def get_model_path(self):
        return self.model_path


if __name__ == '__main__':
    model = TextCorrectionModel()
    model.train("C:\\Users\\karen\\PhD\\SpellCorrectorENG\\Archive\\big.txt")