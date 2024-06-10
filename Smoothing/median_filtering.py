import cv2
import numpy as np
import math




image_path = 'gray.jpeg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
array_2d = np.array(gray_image)

dx = np.zeros_like(array_2d)




