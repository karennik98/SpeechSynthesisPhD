# Import the librosa library
import librosa
import numpy as np
# Import the soundfile library
import soundfile as sf

# Load an audio file
audio_file = 'C:\\Users\\karen\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\tmp\\temp.wav'
audio_data, sample_rate = librosa.load(audio_file)

# Compute the short-time Fourier transform
stft = librosa.stft(audio_data)

# Compute the magnitude spectrum
magnitude = np.abs(stft)

# Compute the spectral flux
flux = np.diff(magnitude, axis=1)
flux = np.pad(flux, ((0, 0), (1, 0)), mode="constant")

# Normalize the spectral flux
flux = (flux - flux.min()) / (flux.max() - flux.min())

# Define a threshold for onset detection
threshold = 0.2

# Find the indices of the onsets
onsets = np.where(flux > threshold)[1]

# Convert the indices to time values
onset_times = librosa.frames_to_time(onsets, sr=sample_rate)

# Segment the audio data based on the onset times
segments = []
start = 0
for end in onset_times:
  segment = audio_data[int(start):int(end)]
  segments.append(segment)
  start = end

output_dir = 'C:\\Users\\karen\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\output_3\\'
# Save the segments as separate audio files
for i, segment in enumerate(segments):
  out_file = output_dir + "segment_{}.wav".format(i)
  sf.write(out_file, segment, sample_rate)
