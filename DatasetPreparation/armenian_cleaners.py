import re

# Regular expression for Armenian numbers
_armenian_numbers = re.compile(r'(\d+)')

# Armenian alphabet and some common punctuation
_armenian_alphabet = set('աբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցւփքևօֆԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔԵՎՕՖ')
_armenian_punctuations = set('։՝՜՞:,.!?')


def _armenian_num2words(number):
    """Convert a number to its Armenian word representation."""
    if not 0 <= number <= 999999999999:
        return "Number out of range (0-999,999,999,999)"

    units = ["", "մեկ", "երկու", "երեք", "չորս", "հինգ", "վեց", "յոթ", "ութ", "ինը"]
    teens = ["տաս", "տասնմեկ", "տասներկու", "տասներեք", "տասնչորս", "տասնհինգ", "տասնվեց", "տասնյոթ", "տասնութ", "տասնինը"]
    tens = ["", "", "քսան", "երեսուն", "քառասուն", "հիսուն", "վաթսուն", "յոթանասուն", "ութսուն", "իննսուն"]
    scales = ["", "հազար", "միլիոն", "միլիարդ"]

    def convert_group(n, scale):
        if n == 0:
            return ""

        result = []

        if n >= 100:
            result.append(units[n // 100])
            result.append("հարյուր")
            n %= 100

        if n >= 20:
            result.append(tens[n // 10])
            if n % 10 != 0:
                result.append(units[n % 10])
        elif n >= 10:
            result.append(teens[n - 10])
        elif n > 0:
            result.append(units[n])

        if scale > 0 and len(result) > 0:
            result.append(scales[scale])

        return " ".join(result)

    if number == 0:
        return "զրո"

    result = []
    for i in range(4):
        group = (number // (1000 ** i)) % 1000
        if group != 0:
            result.insert(0, convert_group(group, i))

    return " ".join(result).strip()


def _normalize_numbers(text):
    """Convert numbers to words in Armenian."""

    def _num_to_word(match):
        number = int(match.group(0))
        return _armenian_num2words(number)

    return re.sub(_armenian_numbers, _num_to_word, text)


def _remove_non_armenian_characters(text):
    """Remove characters that are not Armenian letters or common punctuation."""
    return ''.join(
        char for char in text if char in _armenian_alphabet or char in _armenian_punctuations or char.isspace())


def _normalize_punctuation(text):
    """Normalize some punctuation."""
    text = text.replace('՝', ',')  # Replace Armenian comma with standard comma
    text = text.replace('։', ':')  # Replace Armenian full stop with colon
    text = text.replace('—', '-')  # Replace em dash with hyphen
    return text


def armenian_cleaners(text):
    """Pipeline for Armenian text cleaning."""
    text = text.lower()
    text = _normalize_numbers(text)
    text = _remove_non_armenian_characters(text)
    text = _normalize_punctuation(text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


# Example usage
if __name__ == "__main__":
    test_text = "Երևանը՝ Հայաստանի մայրաքաղաքը, ունի 1060138 բնակիչ։"
    cleaned_text = armenian_cleaners(test_text)
    print(f"Original: {test_text}")
    print(f"Cleaned:  {cleaned_text}")