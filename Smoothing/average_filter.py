import cv2
import numpy as np


image_path = 'gray.jpeg'
input_image_array = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

smoothed_array = np.zeros_like(input_image_array)

dimension_size = 19
mid = (dimension_size - 1) // 2 
rows, cols = input_image_array.shape

for i in range(1, rows):
    for j in range(1, cols):
        block = input_image_array[i - mid:i + mid, j - mid:j + mid]
        smoothed_array[i, j] = np.sum(block) / dimension_size**2

new_image_path = 'smoothing.jpg'
cv2.imwrite(new_image_path, smoothed_array)

print("Done")









