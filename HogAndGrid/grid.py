import cv2
import numpy as np






import cv2
import numpy as np



# resize image

# grayscale
img_path = 'gray.jpeg'
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)


# resize image to divisible by 8


radius = 1
neighbours = 8
gridX = 8
gridY = 8


# finding index of central pixel
height, width = img.shape
central_i = height / 2
central_j = width / 2
threshold = img[central_i, central_j]

# 





