import os
import csv
import json
from phonemizer import phonemize
# from phonemizer.models import armenian

# Paths
data_folder = "/home/karen/PhD/traning/TTS/hy_data/"
metadata_file = os.path.join(data_folder, "metadata.csv")
phoneme_cache_path = "/home/karen/PhD/traning/TTS/hy_data/phoneme_cache/"

# Create phoneme_cache_path directory if it doesn't exist
os.makedirs(phoneme_cache_path, exist_ok=True)

# Function to generate phonemes for text
def generate_phonemes(text):
    return phonemize(text, language='hy', backend='espeak')

# Function to process metadata and generate phoneme cache
def process_metadata(metadata_file):
    phoneme_cache = {}
    with open(metadata_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        # next(reader)  # Skip header if exists
        for row in reader:
            audio_filename = row[0]  # Assuming the first column is audio filename
            text = row[1]  # Assuming the second column is the corresponding text
            phonemes = generate_phonemes(text)
            phoneme_cache[audio_filename] = phonemes
    return phoneme_cache

# Main function to generate and save phoneme cache
def generate_and_save_phoneme_cache():
    phoneme_cache = process_metadata(metadata_file)
    for audio_filename, phonemes in phoneme_cache.items():
        cache_filename = os.path.join(phoneme_cache_path, f"{audio_filename}.json")
        with open(cache_filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(phonemes, jsonfile, ensure_ascii=False)

# Execute main function
generate_and_save_phoneme_cache()
