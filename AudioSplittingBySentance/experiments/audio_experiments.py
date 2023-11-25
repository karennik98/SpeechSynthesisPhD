import AudioUtilities
from pydub.utils import mediainfo

from pydub import AudioSegment

def stereo_to_mono(input_path, output_path):
    # Load the stereo audio file
    audio = AudioSegment.from_file(input_path)

    # Convert to mono by averaging left and right channels
    mono_audio = audio.set_channels(1)

    # Export the mono audio to a new file
    mono_audio.export(output_path, format="wav")

if __name__ == '__main__':
    # Replace 'input_stereo.wav' and 'output_mono.wav' with your file paths
    input_file_path = 'C:\\Users\\karenn\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\input\\hopopy\\001.wav'
    output_file_path = 'C:\\Users\\karenn\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\input\\hopopy\\001_mono.wav'

    stereo_to_mono(input_file_path, output_file_path)
    info = mediainfo(output_file_path)
    print(info)