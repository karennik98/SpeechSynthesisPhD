import pyttsx3
import time
import Utilities

def Test(original_text):
    # Initialize pyttsx3 TTS engine
    engine = pyttsx3.init()

    # Set TTS model properties
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    voice = engine.getProperty('voice')

    # Set TTS model properties
    engine.setProperty('rate', rate-50)
    engine.setProperty('volume', volume+0.25)

    # Set TTS model voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Generate TTS output
    engine.say(original_text)
    engine.runAndWait()
    time.sleep(1)

    # Get TTS model output
    model_output = engine.getProperty('utterance_id')

    # Calculate WER
    wer_metric = Utilities.wer(original_text, model_output)

    print("WER:", wer_metric)
