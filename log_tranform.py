from scipy.ndimage import gaussian_filter
import numpy as np
import cv2


image_path = 'gray.jpeg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
result = np.zeros_like(gray_image)


height, width = gray_image.shape


c = 255 / (np.log(1 + np.max(gray_image)))
log_transofmred = c * np.log(1 + gray_image)

log_transofmred = np.array(log_transofmred, dtype = np.uint8)

cv2.imwrite('log_transformed.jpg', log_transofmred)

print("done")