import cv2
import numpy as np

image_path = 'gray.jpeg'
input_image_array = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

kernel_size = 15
sigma = 2.7

gaussian_kernel = cv2.getGaussianKernel(kernel_size, sigma)
gaussian_mask = gaussian_kernel * gaussian_kernel.T
padded_image = cv2.copyMakeBorder(input_image_array, kernel_size // 2, kernel_size // 2, kernel_size // 2, kernel_size // 2, cv2.BORDER_CONSTANT)

gaussian_filter = np.zeros_like(input_image_array)

rows, cols = input_image_array.shape

for i in range(rows):
    for j in range(cols):
        roi = padded_image[i:i+kernel_size, j:j+kernel_size]
        conv_result = np.sum(roi * gaussian_mask)
        gaussian_filter[i, j] = conv_result

result = 'gaussian_filter.jpg'
cv2.imwrite(result, gaussian_filter)

print("Done")
