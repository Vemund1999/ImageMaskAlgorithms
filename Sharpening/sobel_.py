import cv2
import numpy as np

image_path = 'gray.jpeg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


sobel = np.zeros(img.shape)

height, width = img.shape




for i in range(1, height - 1):
    for j in range(1, width - 1):
        dx = (img[i-1,j+1] + 2*img[i,j+1] + img[i+1,j+1]) - (img[i-1,j-1] + 2*img[i,j-1]+ img[i+1,j-1])
        dy = (img[i+1,j-1] + 2*img[i+1,j] +img[i+1,j+1]) - (img[i-1,j-1] + 2*img[i-1,j]+img[i-1,j+1])

        sobel[i,j] = abs(dx) + abs(dy)
                


cv2.imwrite('sobel.jpg', sobel)




print("Done")


