import cv2
import numpy as np

image_path = 'smoothing.jpg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

img = np.array(gray_image)

prewit = np.zeros_like(img, dtype=np.int32)  
sobel = np.zeros_like(img, dtype=np.int32)   

height, width = img.shape




# block = matrix[start_row:end_row, start_col:end_col]

# det betry gange og minus pluss indekser

for i in range(1, height - 1):
    for j in range(1, width - 1):
        prewit[i,j] = ( - img[i-1,j-1] - img[i,j] - img[i-1,j+1] + img[i+1,j-1] + img[i+1,j] + img[i+1,j+1] )
        sobel[i,j] = ( - img[i-1,j-1] - img[i,j]*2 - img[i-1,j+1] + img[i+1,j-1] + img[i+1,j]*2 + img[i+1,j+1] )

                


cv2.imwrite('prewit.jpg', prewit)
cv2.imwrite('sobel.jpg', sobel)




print("Done")



# make 2d array
#copy of 2d image
