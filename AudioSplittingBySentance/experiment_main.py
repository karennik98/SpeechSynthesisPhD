# import librosa
#
# # Load the audio file
audio_file = 'C:\\Users\\karen\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\tmp\\temp.wav'
# audio, sr = librosa.load(audio_file, sr=None)
#
# # Set a threshold for silence detection (adjust as needed)
# threshold = 0.01
#
# # Find silent intervals
# silent_intervals = librosa.effects.split(audio, top_db=threshold)
#
# # Compute silence lengths
# silence_lengths = [librosa.get_duration(y=audio[interval[0]:interval[1]], sr=sr) for interval in silent_intervals]
#
# # Find the maximum silence length
# max_silence_length = max(silence_lengths)
#
# # Print the maximum silence length in seconds
# print("Max silence length:", max_silence_length, "seconds")


# # Import the modules
# import scipy.io.wavfile as wav
# import numpy as np
# from pydub import AudioSegment
#
# # Read the audio file
# rate, data = wav.read(audio_file)
#
# # Convert to mono if stereo
# if len(data.shape) > 1:
#     data = data[:,0]
#
# # Find the indices where data is non-zero
# non_silence_indices = np.argwhere(data != 0)
#
# # Find the start and end indices of silent segments
# start_indices = np.argwhere(np.diff(non_silence_indices, axis=0) > 1)
# end_indices = start_indices + 1
#
# # Find the durations of silent segments in seconds
# durations = (non_silence_indices[end_indices] - non_silence_indices[start_indices]) / rate
#
# # Find the maximum duration and its index
# max_duration = np.max(durations)
# max_index = np.argmax(durations)
#
# # Find the start and end time of the longest silent segment in seconds
# #start_time = non_silence_indices[start_indices[max_index]] / rate
# #end_time = non_silence_indices[end_indices[max_index]] / rate
#
# # Print the results
# print(f"The maximum length of silence is {max_duration} seconds")
# #print(f"It occurs from {start_time[0][0]:.2f} to {end_time[0][0]:.2f} seconds")
#
# # Load the audio file using pydub
# sound = AudioSegment.from_wav(audio_file)
#
# # Get the loudness in dBFS
# loudness = sound.dBFS
#
# # Print the result
# print(f"The minimum silence threshold is {loudness:.2f} dBFS")


#Importing library and thir function
from pydub import AudioSegment
from pydub.silence import split_on_silence

#reading from audio mp3 file
sound = AudioSegment.from_wav(audio_file)

# spliting audio files
audio_chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-40 )

#loop is used to iterate over the output list
output_dir = 'C:\\Users\\karen\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\output_4\\'
for i, chunk in enumerate(audio_chunks):
   out_file = output_dir + "segment_{}.wav".format(i)
   print("Exporting file", out_file)
   chunk.export(out_file, format="wav")
