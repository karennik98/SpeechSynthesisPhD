from PIL import Image, ImageDraw, ImageFont

text = "Hello, world!"
font_path = "arial.ttf"
font_size = 20

# Create a font object
font = ImageFont.truetype(font_path, font_size)

# Get the size of the text
text_width, text_height = font.getsize(text)

# Define the background color
background_color = (255, 237, 201)  # A light beige color

# Define the size of the background rectangle
bg_width = text_width + 20
bg_height = text_height + 20

# Create an image with the background color and size
img = Image.new('RGB', (bg_width, bg_height), color=background_color)

# Create a drawing context
draw = ImageDraw.Draw(img)

# Draw a rectangle with the background color
draw.rectangle((0, 0, bg_width, bg_height), fill=background_color)

# Write the text onto the image
draw.text((10, 10), text, fill='black', font=font)

# Save the image
img.save('output.png')
