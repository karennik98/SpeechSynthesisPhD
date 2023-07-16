import Config
import Utilites

import pydub
from pydub.silence import detect_silence
import wave

def split_audio_by_silence(audio_file, silence_threshold, silence_length):
    audio = pydub.AudioSegment.from_file(audio_file)
    silences = pydub.silence.detect_silence(audio, min_silence_len=silence_threshold, silence_thresh=silence_length)
    split_files = []
    i = 0
    for start, end in silences:
        audio_path = Config.experiments_output_dir_path + "split_audio_{}.wav".format(i)
        i+=1
        split_file = audio[start:end].export(audio_path, format="wav")
        split_files.append(split_file)
    return split_files

if __name__ == "__main__":
    audio_file = Config.adamamutin_file_path_wav
    silence_threshold = -35
    silence_length = 1075
    split_files = split_audio_by_silence(audio_file, silence_threshold, silence_length)
    for split_file in split_files:
      print(split_file)
