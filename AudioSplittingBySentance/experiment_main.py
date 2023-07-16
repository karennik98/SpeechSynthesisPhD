import Config
import Utilites


if __name__ == '__main__':
    pauses = Utilites.get_pauses(Config.wav_file_path)
    for pause in pauses:
        print(f"Pause: {pause}")
    print(f"Average: {round(sum(pauses)/len(pauses))}")