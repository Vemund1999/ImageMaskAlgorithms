import cv2
import numpy as np

image_path = 'gray.jpeg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

array_2d = np.array(gray_image)

sharp_array = np.zeros_like(array_2d)
dx = np.zeros_like(array_2d)
dy = np.zeros_like(array_2d)


height, width = array_2d.shape

for i in range(1, height - 1):
    for j in range(1, width - 1):
        dx[i,j] = array_2d[i+1, j] - array_2d[i, j]
        dy[i,j] = array_2d[i, j] - array_2d[i, j+1]

        gradient_magnitude = np.sqrt(dx[i,j]**2 + dy[i,j]**2)

        sharp_array[i, j] = array_2d[i, j] + gradient_magnitude

cv2.imwrite('dx.jpg', dx)
cv2.imwrite('dy.jpg', dy)
cv2.imwrite('derivatives_sharpening_of_gray.jpg', sharp_array)

print("Done")



# make 2d array
#copy of 2d image
