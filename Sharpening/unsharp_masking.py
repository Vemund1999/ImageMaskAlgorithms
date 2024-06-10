import cv2
import numpy as np

image_path1 = 'smoothing.jpg'
image_path2 = 'gray.jpeg'

gray_image = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)
smoothing_image = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)

array_2d = np.array(gray_image)

sharp_array = np.zeros_like(array_2d)

height, width = array_2d.shape

for i in range(1, height - 1):
    for j in range(1, width - 1):
        dx = array_2d[i, j + 1] - array_2d[i, j - 1]
        dy = array_2d[i + 1, j] - array_2d[i - 1, j]

        gradient_magnitude = np.sqrt(dx**2 + dy**2)

        sharp_array[i, j] = array_2d[i, j] + gradient_magnitude


cv2.imwrite('derivatives_sharpening_of_smoothing.jpg', sharp_array)

print("Done")
