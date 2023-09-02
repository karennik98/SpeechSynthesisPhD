import Utilites
import TextUtilities
import AudioUtilities
import Config
import csv
import os

if __name__ == "__main__":
    speed_margin = 10
    matched_pairs = []

    AudioUtilities.convert_to_wav(Config.adamamutin_file_path_mp3, Config.adamamutin_file_path_wav)
    words_per_second = AudioUtilities.get_WPS(Config.adamamutin_file_path_wav, Config.adamamutin_docx_file_path)
    print(f"WPS: {words_per_second}")

    text = TextUtilities.read_docx_file(Config.adamamutin_docx_file_path)
    sentences = TextUtilities.split_sentences(text)

    pauses = AudioUtilities.get_pauses(Config.adamamutin_file_path_wav)
    average_silence_len = round(sum(pauses)/len(pauses))
    average_silence_thresh = round(AudioUtilities.get_average_loudness(Config.adamamutin_file_path_wav))
    print(f"Average_silence_len: {average_silence_len}")
    print(f"Average_silence_thresh: {average_silence_thresh}")
    audio_chunks = AudioUtilities.get_audio_chunks(Config.adamamutin_file_path_mp3, average_silence_len, average_silence_thresh)
    saved_audio_files_path = AudioUtilities.save_audio_files(audio_chunks, Config.adamamutin_output_dir_path)

    # Open a CSV file for writing
    with open(Config.adamamutin_output_csv_dir_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter="|")
        change_index = 0
        for sentence, audio_file in zip(sentences, saved_audio_files_path):
            is_match = Utilites.compare_text_audio(sentence, audio_file, words_per_second, tolerance=3.40)
            writer.writerow([os.path.basename(audio_file), sentence])
            temp_sentence=""
            if is_match:
                print("Text matches with audio.")
                # writer.writerow([Utilites.increment_string(os.path.basename(audio_file), change_index), sentence])
            else:
                print("Text does not match with audio.")
                #temp_sentence = AudioUtilities.split_text_by_smth(sentence, audio_file, words_per_second)
                #print(f"temp_sentence: {temp_sentence}")
               # writer.writerow([Utilites.increment_string(os.path.basename(audio_file), change_index), sentence.replace(temp_sentence, "")])
                #change_index += 1
                # if os.path.isfile(audio_file):
                #     os.remove(audio_file)
                #     print("File deleted successfully")
                # else:
                #     print("File not found")
            #if len(temp_sentence) != 0:
            #    writer.writerow([Utilites.increment_string(os.path.basename(audio_file), change_index), temp_sentence])
            print("\n")

    # similarity = Utilites.feature_based_matching(saved_audio_files_path[0], sentences[0])
    # print(f"Similarity: {similarity}")


    # # # Print the sentences
    # # for sentence in sentences:
    # #     print(sentence.strip())
    # #     print(Utilites.get_text_speed(sentence.strip()))
    #
    # audio_chunks = Utilites.get_audio_chunks(Config.audio_file_path)
    #
    # for audio in audio_chunks:
    #     audio_speed = Utilites.get_audio_speaker_speed(audio, Utilites.get_audio_sample_rate(Config.audio_file_path))
    #     best_match = None
    #     min_diff = float("inf")
    #     for sentence in sentences:
    #         text_speed = Utilites.get_text_speed(sentence.strip())
    #         diff = abs(audio_speed - text_speed) / audio_speed * 100
    #
    #         if diff < min_diff and diff < speed_margin:
    #             best_match = sentence
    #             min_diff = diff
    #     if best_match:
    #         matched_pairs.append((audio, best_match))
    #
    # for pair in matched_pairs:
    #     print(pair)

