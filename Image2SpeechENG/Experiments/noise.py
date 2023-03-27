import numpy as np
import cv2

# Define the size of the image
image_width = 640
image_height = 480

# Create a white image with the specified size
image = np.full((image_height, image_width, 3), 255, dtype=np.uint8)

# Add salt-and-pepper noise to the image
noise_amount = 0.05  # adjust this value to control the amount of noise
noise = np.random.choice([0, 1, 2], size=(image_height, image_width), p=[1 - noise_amount, noise_amount/2, noise_amount/2])
image[noise == 1] = 0  # set pixels to black for "salt" noise
image[noise == 2] = 255  # set pixels to white for "pepper" noise

# Display the image
cv2.imshow("Noisy image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2

# Define the size of the image
image_width = 640
image_height = 480

# Create a yellow image with the specified size
image = np.full((image_height, image_width, 3), (0, 255, 255), dtype=np.uint8)

# Add Gaussian noise to the image
mean = 0
stddev = 50  # adjust this value to control the amount of noise
noise = np.random.normal(mean, stddev, (image_height, image_width, 3)).astype(np.uint8)
image = cv2.add(image, noise)

# Display the image
cv2.imshow("Noisy image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

