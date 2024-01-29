import AudioUtilities
from pydub.utils import mediainfo
from pydub import AudioSegment
import GeneralUtilities
import scipy.io.wavfile as wav
from scipy.signal import resample
import soundfile as sf
import librosa
import AudioUtilities

def change_sample_rate(input_file, output_file, new_rate):
    # Read the .wav file
    old_rate, data = wav.read(input_file)

    # Calculate the resample ratio
    resample_ratio = new_rate / old_rate
    # Resample the data
    resampled_data = resample(data, int(len(data) * resample_ratio))

    # Write the output file
    sf.write(output_file, resampled_data, new_rate)


def chnage_sample_rate_2(input_file, output_file):
    y, sr = librosa.load(input_file, sr=None)
    y_downsampled = librosa.resample(y, sr, 22050)
    librosa.output.write_wav(output_file, y_downsampled, 22050)


def stereo_to_mono(input_path, output_path):
    # Load the stereo audio file
    audio = AudioSegment.from_file(input_path)

    # Convert to mono by averaging left and right channels
    mono_audio = audio.set_channels(1)

    # Export the mono audio to a new file
    mono_audio.export(output_path, format="wav")


if __name__ == '__main__':
    # Replace 'input_stereo.wav' and 'output_mono.wav' with your file paths
    input_file_path_mp3 = 'C:\\Users\\karenn\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\experiments\\assets\\common_voice_hy.mp3'
    input_file_path = 'C:\\Users\\karenn\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\experiments\\assets\\audio_lj_speech.wav'
    output_file_path = 'C:\\Users\\karenn\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\output\\adamamutin_anahit_kirakosyan\\wavs\\segment_0_smaple.wav'
    # AudioUtilities.convert_to_wav(input_file_path_mp3, input_file_path)
    # change_sample_rate(input_file_path, output_file_path, 22050)
    # chnage_sample_rate_2(input_file_path, output_file_path)
    # stereo_to_mono(input_file_path, output_file_path)
    # info = mediainfo(output_file_path)
    info = mediainfo(input_file_path)
    print(info)
    GeneralUtilities.save_json_data(info,
                                    'C:\\Users\\karenn\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\experiments\\assets\\audio_lj_speech_metadata.json')
