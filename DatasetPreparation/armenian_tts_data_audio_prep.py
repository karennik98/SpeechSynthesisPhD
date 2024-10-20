import os
import csv
from pydub import AudioSegment
from pydub.silence import split_on_silence
import librosa
import soundfile as sf
import numpy as np


class ArmenianAudioPreprocessor:
    def __init__(self, input_dir, output_dir, metadata_file, target_sr=22050, target_db=-23.0):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.metadata_file = metadata_file
        self.target_sr = target_sr
        self.target_db = target_db

    def process_dataset(self):
        os.makedirs(self.output_dir, exist_ok=True)

        with open(self.metadata_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                if len(row) != 3:
                    print(f"Skipping invalid row: {row}")
                    continue

                filename, _, _ = row
                input_path = os.path.join(self.input_dir, f"{filename}.wav")
                output_path = os.path.join(self.output_dir, f"{filename}.wav")

                if not os.path.exists(input_path):
                    print(f"File not found: {input_path}")
                    continue

                self.process_audio_file(input_path, output_path)

    def process_audio_file(self, input_path, output_path):
        try:
            # Load audio file
            audio, sr = librosa.load(input_path, sr=None)

            # Resample if necessary
            if sr != self.target_sr:
                audio = librosa.resample(audio, sr, self.target_sr)

            # Normalize volume
            audio = self.normalize_volume(audio)

            # Trim silence
            audio = self.trim_silence(audio)

            # Save processed audio
            sf.write(output_path, audio, self.target_sr)
            print(f"Processed: {input_path} -> {output_path}")
        except Exception as e:
            print(f"Error processing {input_path}: {str(e)}")

    def normalize_volume(self, audio):
        target_rms = 10 ** (self.target_db / 20)
        rms = np.sqrt(np.mean(audio ** 2))
        audio = audio * (target_rms / rms)
        return np.clip(audio, -1, 1)

    def trim_silence(self, audio, threshold_db=-50, min_silence_len=200):
        # Convert to pydub AudioSegment for easier silence detection
        audio_segment = AudioSegment(
            audio.tobytes(),
            frame_rate=self.target_sr,
            sample_width=audio.dtype.itemsize,
            channels=1
        )

        # Split on silence and combine non-silent chunks
        chunks = split_on_silence(
            audio_segment,
            min_silence_len=min_silence_len,
            silence_thresh=threshold_db,
            keep_silence=100  # Keep 100ms of silence on either end
        )

        if not chunks:
            return audio

        # Combine chunks and convert back to numpy array
        trimmed_audio = sum(chunks)
        return np.array(trimmed_audio.get_array_of_samples()) / 32768.0  # Normalize to [-1, 1]


if __name__ == "__main__":
    input_dir = "path/to/your/input/wavs"
    output_dir = "path/to/your/output/wavs"
    metadata_file = "path/to/your/metadata.csv"

    preprocessor = ArmenianAudioPreprocessor(input_dir, output_dir, metadata_file)
    preprocessor.process_dataset()