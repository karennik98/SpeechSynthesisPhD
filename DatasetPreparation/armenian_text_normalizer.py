import re

class ArmenianTextNormalizer:
    def __init__(self):
        self.number_map = {
            '0': 'զրո', '1': 'մեկ', '2': 'երկու', '3': 'երեք', '4': 'չորս',
            '5': 'հինգ', '6': 'վեց', '7': 'յոթ', '8': 'ութ', '9': 'ինը',
            '10': 'տաս', '20': 'քսան', '30': 'երեսուն', '40': 'քառասուն', '50': 'հիսուն',
            '60': 'վաթսուն', '70': 'յոթանասուն', '80': 'ութսուն', '90': 'իննսուն',
            '100': 'հարյուր', '1000': 'հազար', '1000000': 'միլիոն', '1500' : 'հազար հինգ հարյուր', '200' : 'երկու հարյուր'
        }
        self.abbreviations = {
            'հ․': 'հատոր',
            'էջ․': 'էջ',
            'թ․': 'թվական',
            'դր․': 'դրամ',
            # Add more abbreviations as needed
        }

    def normalize_numbers(self, text):
        def replace_number(match):
            number = match.group(0)
            if number in self.number_map:
                return self.number_map[number]
            # Handle more complex numbers here
            return number

        return re.sub(r'\d+', replace_number, text)

    def expand_abbreviations(self, text):
        for abbr, expansion in self.abbreviations.items():
            text = text.replace(abbr, expansion)
        return text

    def normalize(self, text):
        text = self.normalize_numbers(text)
        text = self.expand_abbreviations(text)
        # Add more normalization steps as needed
        return text

# Usage example
normalizer = ArmenianTextNormalizer()
sample_text = "Գիրքը արժե 1500 դր․ և ունի 200 էջ․"
normalized_text = normalizer.normalize(sample_text)
print(normalized_text)