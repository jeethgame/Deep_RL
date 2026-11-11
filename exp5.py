from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Load the image
img = Image.open('opera_house.jpg')

#convert image to numpy array and print its shape
print(np.array(img).shape)

# displaying original image
plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Original")

#resize image to 500x500 pixels
plt.subplot(2, 2, 2)
plt.imshow(img.resize((500, 500)))
plt.title("Resized")

# flip image horizontally
plt.subplot(2, 2, 3)
plt.imshow(img.transpose(Image.Transpose.FLIP_LEFT_RIGHT))
plt.title("Flipped")

# rotate image by 45 degrees
plt.subplot(2, 2, 4)
plt.imshow(img.rotate(45))
plt.title("Rotated")

# display all images
plt.show()