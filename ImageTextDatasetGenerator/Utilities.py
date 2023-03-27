import nltk
import Config
import numpy as np
import cv2

nltk.download('punkt')

def Text2Sentences(text):
    return nltk.sent_tokenize(text)

def FilterSentencesWithLen(sentences):
    filteredSentences = list()
    for sent in sentences:
        if len(sent) <= Config.maxAllowedSentenceLen:
            filteredSentences.append(sent)
    return filteredSentences

def AddSaltAndPepperNoise(image):
    # Read the input image
    input_image = cv2.imread(image)

    # Add salt-and-pepper noise to the image
    noise_amount = 0.05  # adjust this value to control the amount of noise
    noise = np.random.choice([0, 1, 2], size=input_image.shape[:2],
                             p=[1 - noise_amount, noise_amount / 2, noise_amount / 2])
    input_image[noise == 1] = 0  # set pixels to black for "salt" noise
    input_image[noise == 2] = 255  # set pixels to white for "pepper" noise

    # Write the noisy image to disk
    cv2.imwrite(image, input_image)


def CleanSentences(sentences):
    return [sent.replace('<br /><br />', '') for sent in sentences]