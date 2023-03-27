import glob
from PIL import Image, ImageDraw, ImageFont
import Config
import os
import Utilities

def create_text_file(fileName, sentences):
    with open(Config.textDir + fileName + '.txt', 'w') as file:
        for sent in sentences:
            file.write(sent + '\n')

def create_text_image(sentences, font_path, font_size, width, heigth, image_color, text_color):
    width = int(Config.maxAllowedSentenceLen * Config.fontSize/2)

    img = Image.new('RGB', (width, heigth), color=image_color)

    # Create a drawing context
    draw = ImageDraw.Draw(img)

    # Set the font and font size
    font = ImageFont.truetype(font_path, size=font_size)

    start = 10
    for sentence in sentences:
        draw.text((10, start), sentence, fill=text_color, font=font)
        start += 30

    return img

if __name__ == '__main__':
    all_txt_files = glob.glob("aclImdb//test//neg//*.txt")
    txt_files = all_txt_files[:Config.datasetItemsCount]
    print(txt_files)
    for file_path in txt_files:
        with open(file_path, 'r') as file:
            text = file.read()
            sentences = Utilities.CleanSentences(Utilities.FilterSentencesWithLen(Utilities.Text2Sentences(text)))
            img = create_text_image(sentences, Config.fontPath, Config.fontSize, Config.width, Config.height, (255, 237, 201), (0, 0, 0))
            file_name, file_ext = os.path.splitext(os.path.basename(file_path))
            img.save(Config.imageDir + file_name + Config.imageExt)
            Utilities.AddSaltAndPepperNoise(Config.imageDir + file_name + Config.imageExt)
            create_text_file(file_name, sentences)