import AudioUtilities
import TextUtilities


def compare_text_audio(text, audio_file, words_per_second, pauses_tolerance=2, tolerance=2.0):
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
