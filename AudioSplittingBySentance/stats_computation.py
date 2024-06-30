import os
import numpy as np
from tqdm import tqdm
import librosa

def compute_spectrogram(wav_path, sample_rate=22050, fft_size=1024, hop_length=256, win_length=1024):
    y, sr = librosa.load(wav_path, sr=sample_rate)
    spectrogram = librosa.stft(y, n_fft=fft_size, hop_length=hop_length, win_length=win_length)
    spectrogram = np.abs(spectrogram)
    return spectrogram.T

def compute_statistics(dataset_dir, output_path, sample_rate=22050, fft_size=1024, hop_length=256, win_length=1024):
    all_spectrograms = []
    wav_files = [os.path.join(dataset_dir, f) for f in os.listdir(dataset_dir) if f.endswith('.wav')]
    for wav_path in tqdm(wav_files):
        spectrogram = compute_spectrogram(wav_path, sample_rate, fft_size, hop_length, win_length)
        all_spectrograms.append(spectrogram)
    all_spectrograms = np.concatenate(all_spectrograms, axis=0)
    mean = np.mean(all_spectrograms, axis=0)
    std = np.std(all_spectrograms, axis=0)
    np.save(output_path, {'mean': mean, 'std': std})

# Example usage
dataset_dir = "/home/karen/PhD/traning/TTS/hy_data/wavs"  # Path to your directory containing WAV files
output_path = "/home/karen/PhD/traning/TTS/hy_data/stats/scale_stats.npy"
compute_statistics(dataset_dir, output_path)
