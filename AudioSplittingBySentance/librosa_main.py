from scipy.io.wavfile import write as write_wav
import numpy as np
import librosa

def zero_runs(a):
    iszero = np.concatenate(([0], np.equal(a, 0).view(np.int8), [0]))
    absdiff = np.abs(np.diff(iszero))
    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
    return ranges

def split_in_parts(audio_path, out_dir):
    # Some constants
    min_length_for_silence = 0.5 # seconds
    percentage_for_silence = 0.98 # eps value for silence
    required_length_of_chunk_in_seconds = 1 # Chunk will be around this value not exact
    sample_rate = 16000 # Set to None to use default

    # Load audio
    waveform, sampling_rate = librosa.load(audio_path, sr=sample_rate)

    # Create mask of silence
    eps = waveform.max() * percentage_for_silence
    silence_mask = (np.abs(waveform) < eps).astype(np.uint8)

    # Find where silence start and end
    runs = zero_runs(silence_mask)
    lengths = runs[:, 1] - runs[:, 0]

    # Left only large silence ranges
    min_length_for_silence = min_length_for_silence * sampling_rate
    large_runs = runs[lengths > min_length_for_silence]
    lengths = lengths[lengths > min_length_for_silence]

    # Mark only center of silence
    silence_mask[...] = 0
    for start, end in large_runs:
        center = (start + end) // 2
        silence_mask[center] = 1

    min_required_length = required_length_of_chunk_in_seconds * sampling_rate
    chunks = []
    prev_pos = 0
    for i in range(min_required_length, len(waveform), min_required_length):
        start = i
        end = i + min_required_length
        next_pos = start + silence_mask[start:end].argmax()
        part = waveform[prev_pos:next_pos].copy()
        prev_pos = next_pos
        if len(part) > 0:
            chunks.append(part)

    # Add last part of waveform
    part = waveform[prev_pos:].copy()
    chunks.append(part)
    print('Total chunks: {}'.format(len(chunks)))

    new_files = []
    for i, chunk in enumerate(chunks):
        out_file = out_dir + "chunk_{}.wav".format(i)
        print("exporting", out_file)
        write_wav(out_file, sampling_rate, chunk)
        new_files.append(out_file)

    return new_files


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # audio_file = 'C:\\Users\\karen\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\input\\audio.mp3'
    audio_file = 'C:\\Users\\karen\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\tmp\\temp.wav'
    output_dir = 'C:\\Users\\karen\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\output\\'

    split_in_parts(audio_file, output_dir)
