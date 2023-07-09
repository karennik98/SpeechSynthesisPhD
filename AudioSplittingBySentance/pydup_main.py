from pydub import AudioSegment
from pydub.silence import split_on_silence

audio_file = 'C:\\Users\\karen\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\tmp\\temp.wav'

sound_file = AudioSegment.from_wav(audio_file)
audio_chunks = split_on_silence(sound_file,
    # must be silent for at least half a second
    min_silence_len=1499,

    # consider it silent if quieter than -16 dBFS
    silence_thresh=-18
)

for i, chunk in enumerate(audio_chunks):
    output_dir = 'C:\\Users\\karen\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\output_2\\'
    out_file = output_dir + "chunk_{}.wav".format(i)
    print("exporting", out_file)
    chunk.export(out_file, format="wav")