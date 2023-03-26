import glob
from PIL import Image, ImageDraw, ImageFont
import Config
import os
import nltk

nltk.download('punkt')  # Download the necessary NLTK data

txt_files = glob.glob("aclImdb//test//neg//*.txt")
print(txt_files)

def create_text_image(text, font_path, font_size, width, heigth, image_color, text_color):
    # Create a new image with the specified size and color
    sentences = nltk.sent_tokenize(text)
    max_len = 0
    for sent in sentences:
        if len(sent) > max_len:
            max_len = len(sent)
    width = int(max_len * Config.fontSize/2)

    img = Image.new('RGB', (width, heigth), color=image_color)

    # Create a drawing context
    draw = ImageDraw.Draw(img)

    # Set the font and font size
    font = ImageFont.truetype(font_path, size=font_size)

    # Write the text onto the image
    sentences = nltk.sent_tokenize(text)
    start = 10
    for sentence in sentences:
        draw.text((10, start), sentence, fill=text_color, font=font)
        start += 30

    # Return the image
    return img

for file_path in txt_files:
    with open(file_path, 'r') as file:
        data = file.read()
        img = create_text_image(data, Config.fontPath, Config.fontSize, Config.width, Config.height, (255, 255, 255), (0, 0, 0))
        file_name, file_ext = os.path.splitext(os.path.basename(file_path))
        img.save(Config.imageDir + file_name + Config.imageExt)