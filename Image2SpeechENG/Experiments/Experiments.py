from PIL import Image, ImageDraw, ImageFilter, ImageOps

# Open the input image
input_image = Image.open("old_book.jpg")

# Create a new image with the same size as the input image
output_image = Image.new("RGBA", input_image.size)

# Load the book texture image
texture_image = Image.open("old_book.jpg")

# Resize the book texture image to match the size of the input image
texture_image = texture_image.resize(input_image.size)

# Blend the book texture image with the input image
output_image = Image.blend(input_image, texture_image, 0.6)

# Add a border around the image to simulate the edges of a book page
border_size = int(min(output_image.size) * 0.05)
output_image = ImageOps.expand(output_image, border_size, "white")

# Apply a Gaussian blur to the image to give it a softer look
output_image = output_image.filter(ImageFilter.GaussianBlur(radius=3))

# Save the output image
output_image.save("output_image.jpg")
