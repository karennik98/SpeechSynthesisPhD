from phonemizer import phonemize
from phonemizer.backend import EspeakBackend


class ArmenianPhonemizer:
    def __init__(self):
        self.backend = EspeakBackend('hy')  # 'hy' is the language code for Armenian

    def phonemize(self, text):
        return phonemize(
            text,
            language='hy',
            backend='espeak',
            strip=True,
            preserve_punctuation=True,
            with_stress=False,
            punctuation_marks=';:,.!?¡¿—…"«»""'
        )


# Test the phonemizer
# if __name__ == "__main__":
#     phonemizer = ArmenianPhonemizer()
#     test_texts = [
#         "Բարև Ձեզ",
#         "Ինչպե՞ս եք",
#         "Հայաստան",
#         "Երևան քաղաքը մայրաքաղաքն է"
#     ]
#
#     for text in test_texts:
#         phonemes = phonemizer.phonemize(text)
#         print(f"Original: {text}")
#         print(f"Phonemes: {phonemes}")
#         print()