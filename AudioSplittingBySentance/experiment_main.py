import numpy as np
import Config
from python_speech_features import mfcc
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

def calculate_distance(x, y):
    # Calculate the distance between two MFCC feature vectors
    return euclidean(x, y)

def align_audio_text(audio_file, text):
    # Extract MFCC features from the audio file
    audio_features = extract_mfcc_features(audio_file)

    # Convert text to MFCC features
    text_features = text_to_mfcc_features(text)

    # Apply DTW to align the audio and text
    distance, path = fastdtw(audio_features, text_features, dist=calculate_distance)

    # Calculate the alignment score based on the distance
    alignment_score = -distance / len(path)

    return alignment_score

def extract_mfcc_features(audio_file):
    # Extract MFCC features from the audio file
    # Modify this function based on the audio processing library you are using
    # For example, you can use librosa or pydub to extract audio features
    # Here, we are using python_speech_features library
    # Make sure you have the necessary dependencies installed

    # Read audio file and convert to feature vectors
    # Here, we are using the default parameters of MFCC extraction
    # Modify the parameters according to your requirements
    audio, sample_rate = read_audio_file(audio_file)
    features = mfcc(audio, sample_rate)

    return features

def text_to_mfcc_features(text):
    # Convert text to MFCC features
    # Modify this function based on how you want to represent text as MFCC features
    # You can use techniques like one-hot encoding, vector embeddings, etc.
    armenian_lowercase = ['ա', 'բ', 'գ', 'դ', 'ե', 'զ', 'է', 'ը', 'թ', 'ժ', 'ի', 'լ', 'խ', 'ծ', 'կ', 'հ', 'ձ', 'ղ', 'ճ',
                          'մ', 'յ', 'ն', 'շ', 'ո', 'չ', 'պ', 'ջ', 'ռ', 'ս', 'վ', 'տ', 'ր', 'ց', 'ու', 'փ', 'ք', 'և',
                          'օ', 'ֆ']
    # Here, we are simply converting each character to a fixed-length vector of zeros and ones
    text_features = []
    for char in text:
        if char.lower() not in armenian_lowercase:
            continue
        vector = [0] * 36  # Assuming 26 alphabets
        index = ord(char.lower()) - ord('ա')
        vector[index] = 1
        text_features.append(vector)

    return text_features

def read_audio_file(audio_file):
    # Read audio file and return audio signal and sample rate
    # Modify this function based on the audio processing library you are using
    # For example, you can use librosa or pydub to read audio files

    # Here, we are using a placeholder function that returns dummy values
    # Replace it with the appropriate code to read the audio file
    dummy_audio = np.random.rand(10000)  # Dummy audio signal
    sample_rate = 44100  # Placeholder sample rate

    return dummy_audio, sample_rate

# Example usage
audio_file = "C:\\Users\\karen\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\output\\adamamutin_anahit_kirakosyan\\wavs\\segment_1.wav"  # Path to audio file
text = "Այդ տուն կոչվածը մի բավական մեծ խրճիթ էր, որ երբեմն տիրոջ կթան կովերի համար գոմի տեղ էր ծառայում:"  # Text to compare with audio

alignment_score = align_audio_text(audio_file, text)

print(f"Alignment Score: {alignment_score}")


