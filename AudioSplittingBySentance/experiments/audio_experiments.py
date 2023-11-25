import AudioUtilities
from pydub.utils import mediainfo

if __name__ == '__main__':
    info = AudioUtilities.get_audio_info("C:\\Users\\karenn\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\input\\hopopy\\001.wav")
    for key, value in info.items():
        print(f"{key}: {value}")

    info2 = mediainfo("C:\\Users\\karenn\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\input\\hopopy\\001.wav")
    print(info2)