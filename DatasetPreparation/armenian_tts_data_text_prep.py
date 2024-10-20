import csv
import os
from armenian_text_normalizer import ArmenianTextNormalizer
from armenian_g2p_converter import ArmenianPhonemizer

class ArmenianTTSDataPrep:
    def __init__(self, input_csv, output_csv):
        self.input_csv = input_csv
        self.output_csv = output_csv
        self.normalizer = ArmenianTextNormalizer()
        self.g2p_converter = ArmenianPhonemizer()

    def process_csv(self):
        with open(self.input_csv, 'r', encoding='utf-8') as infile, \
             open(self.output_csv, 'w', newline='', encoding='utf-8') as outfile:
            reader = csv.reader(infile, delimiter='|')
            writer = csv.writer(outfile, delimiter='|')

            for row in reader:
                if len(row) != 3:
                    print(f"Skipping invalid row: {row}")
                    continue

                file_name, text, normalized_text = row

                # Apply text normalization
                normalized_text = self.normalizer.normalize(normalized_text)

                # Apply G2P conversion
                phonemes = self.g2p_converter.phonemize(normalized_text)

                # Write to output CSV
                writer.writerow([file_name, normalized_text, phonemes])

        print(f"Processed data saved to {self.output_csv}")

    def verify_audio_files(self, audio_dir):
        with open(self.input_csv, 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile, delimiter='|')
            for row in reader:
                if len(row) != 3:
                    continue
                file_name = row[0]
                full_path = os.path.join(audio_dir, file_name + '.wav')
                if not os.path.exists(full_path):
                    print(f"Warning: Audio file not found: {full_path}")

if __name__ == "__main__":
    input_csv = "path/to/your/metadata.csv"
    output_csv = "path/to/your/processed_metadata.csv"
    audio_dir = "path/to/your/wavs"

    data_prep = ArmenianTTSDataPrep(input_csv, output_csv)
    data_prep.process_csv()
    data_prep.verify_audio_files(audio_dir)