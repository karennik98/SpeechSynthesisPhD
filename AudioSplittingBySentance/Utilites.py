import AudioUtilities
import TextUtilities
from dtw import dtw
import librosa

import scipy.spatial.distance
from sklearn.feature_extraction.text import TfidfVectorizer


def feature_based_matching(audio_file_path, text_sentence):
    # Extract the MFCC features from the audio
    audio, sample_rate = librosa.load(audio_file_path)
    mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate)

    # Extract the TF-IDF features from the text
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text_sentence]).toarray()

    # Align the MFCC matrix and the TF-IDF vector using DTW
    dist, cost, path = dtw(mfcc.T, tfidf)
    mfcc_aligned = mfcc[:, path[0]]
    tfidf_aligned = tfidf[0, path[1]]

    # Compute the cosine similarity between the aligned features
    similarity = 1 - scipy.spatial.distance.cosine(mfcc_aligned.flatten(), tfidf_aligned.flatten())
    return similarity

def compare_text_audio(text, audio_file, words_per_second, pauses_tolerance = 2, tolerance=2.0):
    audio_duration = AudioUtilities.calculate_audio_duration(audio_file)
    print(f"Audio duartion for: {audio_file} is: {audio_duration}")
    expected_duration = TextUtilities.calculate_expected_duration(text, words_per_second)
    print(f"Expected duartion for: {text} is: {expected_duration}")

    duration_difference = abs(audio_duration - expected_duration)

    pauses_excpectant = TextUtilities.pauses_expectant(text)
    audio_pauses = len(AudioUtilities.get_pauses(audio_file))
    print(f"Expected pauses count from text: {pauses_excpectant}")
    print(f"Expected pauses count from audio: {audio_pauses}")

    pauses_difference = abs(pauses_excpectant - audio_pauses)

    match = (duration_difference <= tolerance and pauses_difference <= pauses_tolerance)

    return match


import re # import the re module

def increment_string (s, n): # define a function that takes a string and a number as arguments
    # match = re.search (r'\d+', s) # find the first sequence of digits in the string
    # if match: # if there is a match
    #     num = int (match.group ()) # convert the matched digits to an integer
    #     num += n # increment the integer by n
    #     new_s = re.sub (r'\d+', str (num), s) # replace the matched digits with the incremented integer as a string
    #     return new_s # return the new string
    # else: # if there is no match
    #     return s # return the original string
    return s
