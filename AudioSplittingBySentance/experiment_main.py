# # # import numpy as np
# # # import librosa
# # # from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
# # # from sklearn.feature_extraction.text import CountVectorizer
# # # from scipy.stats import pearsonr
# # # from sklearn.preprocessing import RobustScaler
# # # import os
# # #
# # # def extract_audio_features(audio_file):
# # #     y, sr = librosa.load(audio_file)
# # #     mfccs = librosa.feature.mfcc(y=y, sr=sr)
# # #     chroma = librosa.feature.chroma_stft(y=y, sr=sr)
# # #     energy = np.sum(y ** 2)
# # #     zero_crossing_rate = np.sum(np.diff(np.sign(y)) != 0)
# # #     spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
# # #     spectral_spread = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
# # #
# # #     audio_features = np.concatenate([mfccs.mean(axis=1), chroma.mean(axis=1),
# # #                                      [energy, zero_crossing_rate],
# # #                                      [spectral_centroid.mean(), spectral_spread.mean()]])
# # #     return audio_features.reshape(-1, 1)
# # #     #return RobustScaler().fit_transform(audio_features.reshape(1, -1))
# # #
# # #
# # # def extract_text_features(text_transcript):
# # #     vectorizer = CountVectorizer()  # You can also use TfidfVectorizer for TF-IDF
# # #     text_vector = vectorizer.fit_transform([text_transcript])
# # #     return text_vector.reshape(-1, 1)
# # #     #return RobustScaler().fit_transform(text_vector.toarray().flatten().reshape(1, -1))
# # #
# # #
# # # def calculate_similarity(audio_features, text_features):
# # #     cosine_sim = cosine_similarity(audio_features, text_features)
# # #     euclidean_dist = euclidean_distances(audio_features, text_features)
# # #     #pearson_corr, _ = pearsonr(audio_features.flatten(), text_features.flatten())
# # #     return cosine_sim[0][0], euclidean_dist[0][0] #, pearson_corr
# # #
# # #
# # # # Example audio file and transcript
# # # audio_file = "output/adamamutin_anahit_kirakosyan/wavs/segment_0.wav"
# # # text_transcript = "Շուշանը — մի պստիկ, լղար կին — կուչ էր եկել իրենց տան անկյունում:"
# # #
# # # if not os.path.exists(audio_file):
# # #     print("Audio file not found.")
# # # else:
# # #     # Extract features
# # #     audio_features = extract_audio_features(audio_file)
# # #     text_features = extract_text_features(text_transcript)
# # #
# # #     # Calculate similarity metrics
# # #     cosine_sim, euclidean_dist = calculate_similarity(audio_features, text_features)
# # #
# # #     print("Cosine Similarity:", cosine_sim)
# # #     print("Euclidean Distance:", euclidean_dist)
# #
# #
# # from pydub import AudioSegment
# # from pydub.generators import Sine
# #
# # from pydub import AudioSegment, silence
# # from pydub.silence import split_on_silence
# # import pydub
# #
# # import AudioUtilities
# #
# # def get_pauses(audio_file_path):
# #     myaudio = AudioSegment.from_wav(audio_file_path)
# #     dBFS = myaudio.dBFS
# #     silence = pydub.silence.detect_silence(myaudio, min_silence_len=500, silence_thresh=dBFS - 16)
# #     return [(stop - start) for start, stop in silence]
# #
# # def mark_pauses(audio_file_path, output_file_path):
# #     myaudio = AudioSegment.from_wav(audio_file_path)
# #     pauses = get_pauses(audio_file_path)
# #     beep = Sine(1000).to_audio_segment(duration=100) # create a 100 ms beep sound with 1000 Hz frequency
# #     for start, stop in pauses:
# #         myaudio = myaudio.overlay(beep, position=start) # overlay the beep sound at the start of each pause
# #     myaudio.export(output_file_path, format="wav") # export the marked audio file
# #
# # mark_pauses("input/adamamutin_anahit_kirakosyan/001_cut.wav", "marked.wav") # mark the pauses in example.wav and save as marked.wav
#
#
# import whisper
# #
# def whisper_text(audio_path):
#     model = whisper.load_model("base")
#
#     # load audio and pad/trim it to fit 30 seconds
#     audio = whisper.load_audio(audio_path)
#     audio = whisper.pad_or_trim(audio)
#
#     # make log-Mel spectrogram and move to the same device as the model
#     mel = whisper.log_mel_spectrogram(audio).to(model.device)
#
#     # detect the spoken language
#     _, probs = model.detect_language(mel)
#     print(f"Detected language: {max(probs, key=probs.get)}")
#
#     # decode the audio
#     options = whisper.DecodingOptions(fp16=False)
#     result = whisper.decode(model, mel, options)
#
#     # print the recognized text
#     print(result.text)
#
#
# #Import library
# from armspeech import ArmSpeech_STT
# import librosa
# import soundfile
# from pydub import AudioSegment
# def chage_sample_rate(in_audio_file_path, out_audio_file_path, sample_rate=16000):
#     # Load the audio file
#     audio = AudioSegment.from_wav(in_audio_file_path)
#
#     # Change the sample rate to 16000 Hz
#     audio = audio.set_frame_rate(sample_rate)
#
#     # Save the modified audio file
#     audio.export(out_audio_file_path, format="wav")
#
# #Create object
# armspeech_stt = ArmSpeech_STT()
#
# #Transcribe wav audio file
# in_audio_path = "output/adamamutin_anahit_kirakosyan/wavs/segment_0.wav"
# out_audio_path = "tmp/temp_0.wav"
# chage_sample_rate(in_audio_path, out_audio_path)
# result = armspeech_stt.from_wav(wav_path = out_audio_path, get_metadata = True)
# print(result)
# whisper_text(out_audio_path)
#
# # #Start microphone streaming
# # for result in armspeech_stt.from_mic (vad_aggresivness = 2, spinner = True, wav_save_path = 'path/to/transcribed/speeches', get_metadata = False):
# #     print(result)

import os
import csv

already_processed={}
with open("output/adamamutin_anahit_kirakosyan/temp_metadata.csv", "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter="|")
    for audio, text in reader:
        print(audio)
        print(text)
        already_processed[audio] = text