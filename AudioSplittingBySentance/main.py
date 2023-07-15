import Utilites
import Config

if __name__ == "__main__":
    speed_margin = 10
    matched_pairs = []

    wav_file_path = "C:\\Users\\karen\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\input\\002.wav"
    Utilites.convert_to_wav(Config.audio_file_path, wav_file_path)
    wps = Utilites.get_WPS(wav_file_path, Config.docx_file_path)
    print(f"WPS: {wps}")
    words_per_second = wps

    text = Utilites.read_docx_file(Config.docx_file_path)
    sentences = Utilites.split_sentences(text)

    audio_chunks = Utilites.get_audio_chunks(Config.audio_file_path)
    saved_audio_files_path = Utilites.save_audio_files(audio_chunks, Config.output_dir_path)

    for sentence, audio_file in zip(sentences, saved_audio_files_path):
        is_match = Utilites.compare_text_audio(sentence, audio_file, words_per_second)
        if is_match:
            print("Text matches with audio.")
        else:
            print("Text does not match with audio.")
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

