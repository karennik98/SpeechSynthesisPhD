from pydub import AudioSegment
from pydub.playback import play
from fuzzywuzzy import fuzz

def isSame(audio_file, text_reference):
    # Load audio file
    audio = AudioSegment.from_file(audio_file)

    # Convert text to lower case for case-insensitive comparison
    text_reference = text_reference.lower()

    # Define window length (in milliseconds) for audio fingerprinting
    window_length = 1000

    # Calculate number of windows
    num_windows = len(audio) // window_length

    # Create audio fingerprints (using simple amplitude-based fingerprints)
    audio_fingerprints = []
    for i in range(num_windows):
        window = audio[i * window_length : (i + 1) * window_length]
        amplitude_fingerprint = sum(window.get_array_of_samples())  # Simplified fingerprint
        audio_fingerprints.append(amplitude_fingerprint)

    # Simulate matching process
    match_found = False
    matching_threshold = 0.7  # You can adjust this threshold based on your data

    for i, fingerprint in enumerate(audio_fingerprints):
        # Simulate retrieving transcribed text for the matched audio segment
        transcribed_text = text_reference

        # Convert transcribed text to lower case for case-insensitive comparison
        transcribed_text = transcribed_text.lower()

        # Calculate text similarity using fuzzy matching (you can use other methods)
        similarity_score = fuzz.ratio(text_reference, transcribed_text) / 100.0

        if similarity_score > matching_threshold:
            print(f"Match found at window {i}, Similarity: {similarity_score}")
            match_found = True
            break

    return match_found
    # if not match_found:
    #     print("No match found.")
    #
    # # Play the audio segment corresponding to the matched window
    # if match_found:
    #     matched_audio_segment = audio[i * window_length : (i + 1) * window_length]
    #     play(matched_audio_segment)