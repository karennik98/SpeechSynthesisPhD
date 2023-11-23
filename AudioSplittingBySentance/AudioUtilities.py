from pydub import AudioSegment, silence
from pydub.silence import split_on_silence
from docx import Document
import pydub
import wave
import librosa
import TextUtilities
import SimilarityUtilites


def get_pauses(audio_file_path):
    myaudio = AudioSegment.from_wav(audio_file_path)
    dBFS = myaudio.dBFS
    silence = pydub.silence.detect_silence(myaudio, min_silence_len=500, silence_thresh=dBFS - 16)
    return [(stop - start) for start, stop in silence]


def get_average_loudness(audio_file_path):
    audio = AudioSegment.from_wav(audio_file_path)
    return audio.dBFS - 16


def get_audio_speaker_speed(audio_sentence, sample_rate):
    # Calculate the duration of the audio sentence in seconds
    audio_duration = len(audio_sentence) / sample_rate
    # Calculate the number of words in the audio sentence by counting the spaces
    audio_words = audio_sentence.count(" ") + 1
    # Calculate the speed of the speaker in words per minute
    audio_speed = audio_words / audio_duration * 60
    return audio_speed

def get_audio_chunks(audio_path, silence_len, thresh):
    sound = AudioSegment.from_mp3(audio_path)
    audio_chunks = split_on_silence(sound, min_silence_len=silence_len, silence_thresh=thresh)
    return audio_chunks


def get_audio_sample_rate(audio_path):
    sound = AudioSegment.from_mp3(audio_path)
    return sound.frame_rate


def save_audio_files(audio_chunks, output_dir, audio_start_index):
    saved_audio_file_paths = []
    for i, chunk in enumerate(audio_chunks):
        if i < 3:
            continue
        out_file = output_dir + "segment_{}.wav".format(audio_start_index)
        audio_start_index += 1
        chunk.export(out_file, format="wav")
        saved_audio_file_paths.append(out_file)
    return saved_audio_file_paths


def save_audio_file(audio, file_path):
    audio.export(file_path, format="wav")


def convert_to_wav(mp3_file, wav_file):
    audio = pydub.AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format='wav')


def get_WPS(audio_file_path, text_file_path):
    document = Document(text_file_path)
    text = ' '.join([paragraph.text for paragraph in document.paragraphs])
    # Load the audio file and obtain its duration
    with wave.open(audio_file_path, 'rb') as wav:
        frame_rate = wav.getframerate()
        n_frames = wav.getnframes()
        audio_duration = n_frames / frame_rate
    # Count the number of words in the text
    word_count = len(text.split())
    words_per_second = word_count / audio_duration

    return words_per_second


def calculate_audio_duration(audio_file):
    with wave.open(audio_file, 'rb') as wav:
        frame_rate = wav.getframerate()
        n_frames = wav.getnframes()
        audio_duration = n_frames / frame_rate

    return audio_duration


def get_expected_speaking_time(text, WPS):
    return WPS * len(text.split())

def split_text_by_smth(text, audio_file, WPS):
    splits = text.split(',')
    removed_item = ""
    for item in splits:
        match = Utilites.compare_text_audio(item, audio_file, WPS, tolerance=2.0)
        if match:
            removed_item = item
            break
    return text.replace(removed_item, "")