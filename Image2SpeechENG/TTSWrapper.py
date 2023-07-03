import pyttsx3


class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'english-us')

    def say(self, text):
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 100)

        self.engine.say(text)
        self.engine.runAndWait()

    def saveWav(self, text, path):
        self.engine.save_to_file(text, path)
        self.engine.runAndWait()
