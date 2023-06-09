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
    noise_amount = 0.005  # adjust this value to control the amount of noise
    noise = np.random.choice([0, 1, 2], size=input_image.shape[:2],
                             p=[1 - noise_amount, noise_amount / 2, noise_amount / 2])
    input_image[noise == 1] = 0  # set pixels to black for "salt" noise
    input_image[noise == 2] = 255  # set pixels to white for "pepper" noise

    # Write the noisy image to disk
    cv2.imwrite(image, input_image)

def AddGaussianNoise(image_path, noise_stddev=0.6):
    # Load the input image
    image = cv2.imread(image_path)

    # Generate the noise and add it to the image
    noise = np.random.normal(0, noise_stddev, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)

    cv2.imwrite(image_path, noisy_image)


def CleanSentences(sentences):
    return [sent.replace('<br /><br />', '') for sent in sentences]