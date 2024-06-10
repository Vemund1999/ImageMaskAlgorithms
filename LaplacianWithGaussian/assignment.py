import cv2
import numpy as np
from gaussian_filter_mask import apply_gaussian_filter
from laplacian_operator import apply_laplacian_filter


path = 'images/'
image_path = path + 'gray.jpeg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# GAUSSIAN
apply_gaussian_filter(img, path + 'gaussian_filter.jpg')

# ONLY LAPLACIAN
apply_laplacian_filter(img, path + 'laplacian_filter.jpg')

# LAPLACIAN WITH GAUSSIAN
img = cv2.imread(path + 'gaussian_filter.jpg', cv2.IMREAD_GRAYSCALE)
apply_laplacian_filter(img, path + 'laplacian_filter_with_smoothing.jpg')



