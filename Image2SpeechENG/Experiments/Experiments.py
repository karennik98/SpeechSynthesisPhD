# from PIL import Image, ImageDraw, ImageFilter, ImageOps
#
# # Open the input image
# input_image = Image.open("old_book.jpg")
#
# # Create a new image with the same size as the input image
# output_image = Image.new("RGBA", input_image.size)
#
# # Load the book texture image
# texture_image = Image.open("old_book.jpg")
#
# # Resize the book texture image to match the size of the input image
# texture_image = texture_image.resize(input_image.size)
#
# # Blend the book texture image with the input image
# output_image = Image.blend(input_image, texture_image, 0.6)
#
# # Add a border around the image to simulate the edges of a book page
# border_size = int(min(output_image.size) * 0.05)
# output_image = ImageOps.expand(output_image, border_size, "white")
#
# # Apply a Gaussian blur to the image to give it a softer look
# output_image = output_image.filter(ImageFilter.GaussianBlur(radius=3))
#
# # Save the output image
# output_image.save("output_image.jpg")

import pandas as pd

# create four lists with different lengths
list1 = [1, 2, 3, 4]
list2 = ['apple', 'banana', 'orange']
list3 = [10.5, 20.3, 30.1, 40.7, 50.2]
list4 = ['A', 'B']

# pad the shorter lists with None values
max_length = max(len(list1), len(list2), len(list3), len(list4))
list1 += [None] * (max_length - len(list1))
list2 += [None] * (max_length - len(list2))
list3 += [None] * (max_length - len(list3))
list4 += [None] * (max_length - len(list4))

# create a pandas dataframe with the four lists as columns
df = pd.DataFrame({'Column 1 Name': list1,
                   'Column 2 Name': list2,
                   'Column 3 Name': list3,
                   'Column 4 Name': list4})

# write the dataframe to an Excel file on different columns
with pd.ExcelWriter('output.xlsx') as writer:
    for i, column in enumerate(df.columns):
        df[[column]].to_excel(writer, sheet_name='Sheet1', startcol=i, index=False)

