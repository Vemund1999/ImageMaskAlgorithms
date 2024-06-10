import cv2
import numpy as np


image_path = 'gray.jpeg'
input_image_array = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

sharpened_image = np.zeros_like(input_image_array)

mask = [
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]
]
mid = 1
dim = 3*3

rows, cols = input_image_array.shape

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        block = input_image_array[i - mid:i + mid + 1, j - mid:j + mid + 1]
        sharpened_image = np.sum( block * mask ) / dim

result = 'sharpening_filter_mask.jpg'
cv2.imwrite(result, sharpened_image)

print("Done")