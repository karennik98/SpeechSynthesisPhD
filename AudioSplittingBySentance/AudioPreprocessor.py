import Config
import Utilites
import TextUtilities
import AudioUtilities
import csv
import os
import logging


class AudioPrprocessor:

    def __init__(self, mp3_file_path, wav_file_path, docx_file_path, metadata_file_path, out_waves_dir):
        self.logger = logging.getLogger("error_logger AudioPrprocessor")
        self.logger.setLevel(logging.ERROR)
        file_handler = logging.FileHandler("Error.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        if not os.path.exists(mp3_file_path):
            self.logger.error(f"{mp3_file_path} File not exist:")
            return
        if not os.path.exists(docx_file_path):
            self.logger.error(f"{docx_file_path} File not exist:")
            return
        if not os.path.exists(out_waves_dir):
            self.logger.error(f"{out_waves_dir} Directory not exist:")
            return

        self.mp3_file_path = mp3_file_path
        self.wav_file_path = wav_file_path
        self.docx_file_path = docx_file_path
        self.metadata_file_path = metadata_file_path
        self.out_waves_dir = out_waves_dir

    def start(self):
        AudioUtilities.convert_to_wav(self.mp3_file_path, self.wav_file_path)
        words_per_second = AudioUtilities.get_WPS(self.wav_file_path, self.docx_file_path)
        print(f"WPS: {words_per_second}")

        text = TextUtilities.read_docx_file(self.docx_file_path)
        sentences = TextUtilities.split_sentences(text)

        pauses = AudioUtilities.get_pauses(self.wav_file_path)
        average_silence_len = round(sum(pauses) / len(pauses))
        average_silence_thresh = round(AudioUtilities.get_average_loudness(self.wav_file_path))
        print(f"Average_silence_len: {average_silence_len}")
        print(f"Average_silence_thresh: {average_silence_thresh}")
        audio_chunks = AudioUtilities.get_audio_chunks(self.mp3_file_path, average_silence_len,
                                                       average_silence_thresh)
        saved_audio_files_path = AudioUtilities.save_audio_files(audio_chunks, self.out_waves_dir)

        with open(self.metadata_file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter="|")
            for sent, audio_file_name in zip(sentences, saved_audio_files_path):
                writer.writerow([os.path.basename(audio_file_name), sent])
                is_match = Utilites.compare_text_audio(sent, audio_file_name, words_per_second, tolerance=3.40)
                if is_match:
                    print("Text matches with audio.")
                else:
                    print("Text does not match with audio.")
                print("\n")


preproc = AudioPrprocessor(mp3_file_path=Config.adamamutin_file_path_mp3,
                           wav_file_path=Config.adamamutin_file_path_wav,
                           docx_file_path=Config.docx_file_path,
                           metadata_file_path=Config.adamamutin_output_csv_dir_path,
                           out_waves_dir=Config.adamamutin_output_dir_path)

preproc.start()