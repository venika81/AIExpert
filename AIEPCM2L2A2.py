#  Rotating and Adjusting Brightness
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('example.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Rotate the image by 45 degrees around its center
(h, w) = image.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)  # rotate by 45 degrees
rotated = cv2.warpAffine(image, M, (w, h))

rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

# Increase brightness by adding 50 to all pixel values
# Use cv2.add to avoid negative values or overflow
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
brighter = cv2.add(image, brightness_matrix)

brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()
