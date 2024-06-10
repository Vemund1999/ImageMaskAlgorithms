import cv2
import numpy as np

# Read the input image
input_image = cv2.imread('gray.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to the input image
blurred_image = cv2.GaussianBlur(input_image, (5, 5), 0)

# Define Laplacian filter kernel
laplacian_filter = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]])

rows, cols = input_image.shape
sharpened_image = np.zeros_like(input_image)
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        neighborhood = blurred_image[i - 1:i + 2, j - 1:j + 2]
        sharpened_image[i, j] = np.sum(neighborhood * laplacian_filter)

final_image = cv2.add(input_image, sharpened_image)

cv2.imwrite('laplacian_filter.jpg', final_image)

print("Done")