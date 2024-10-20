import librosa
import os


def check_audio_files(dataset_path, min_duration=0.1):
    problematic_files = []
    for root, _, files in os.walk(dataset_path):
        for file in files:
            if file.endswith('.wav'):
                file_path = os.path.join(root, file)
                try:
                    y, sr = librosa.load(file_path)
                    duration = librosa.get_duration(y=y, sr=sr)
                    if duration < min_duration:
                        problematic_files.append((file_path, duration))
                except Exception as e:
                    problematic_files.append((file_path, str(e)))

    return problematic_files


# Usage
dataset_path = "/home/karen/PhD/TTS/hy_tts_train_dir/hy_data/wavs"
problematic_files = check_audio_files(dataset_path)
for file, issue in problematic_files:
    print(f"Issue with file {file}: {issue}")