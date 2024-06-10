import cv2
import numpy as np






import cv2
import numpy as np



# resize image

# grayscale
img_path = 'gray.jpeg'
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)



# =========== RESIZING IMAGE ===========


# =========== APPLYING SOBEL ===========

orientation = np.zeros_like(img, dtype=np.int32)   
magnitude = np.zeros_like(img, dtype=np.int32)

height,width = img.shape

# get oriantation and magnitude
for i in range(1, height - 1):
    for j in range(1, width - 1):
        dx = img[i+1, j] - img[i, j]
        dy = img[i, j] - img[i, j+1]
        orientation[i,j] = np.arctan2(dy, dx)
        magnitude[i,j] = abs(dx + dy)


# =========== divide into 8x8 blocks ===========
orientation_blocks = np.zeros_like(( height / 8, width / 8 ))
magnitude_blocks = np.zeros_like(( height / 8, width / 8 ))
blocks = np.zeros_like(( height / 8, width / 8 ))

# making a histogram list for each block
histograms = np.zeros( len(blocks) )

a = 0
b = 0
height_blocks_of_8, width_blocks_of_8 = blocks.shape
for i in range(0, height_blocks_of_8 - 1):
    for j in range(0, width_blocks_of_8 - 1):
        a = i*8
        b = j*8
        orientation_blocks[i,j] = orientation[a:8+a,b:8+b]
        magnitude_blocks[i,j] = magnitude[a:8+a,b:8+b]
        blocks[i,j] = img[a:8+a,b:8+b] # for the 16x16 block normalization
        # looping the block to fill the histogram
        for k in range(0, width_blocks_of_8 - 1):
            for l in range(0, height_blocks_of_8 - 1):
                index_over = None
                index_under = None
                if (orientation_blocks[i,j][k,l] <= 160):
                    index_under = abs(orientation_blocks[i,j][k,l] / 20)
                    index_over = abs(orientation_blocks[i,j][k,l] / 20) + 1
                    percent = (index_under - magnitude_blocks[i,j][k,l]) / 20
                else:
                    index_under = 0
                    index_over = 1
                    percent = (index_over - magnitude_blocks[i,j][k,l]) / 20
                    
                histograms[k,l][index_under] = magnitude_blocks[i,j][k,l]*(1-percent)
                histograms[k,l][index_over] = magnitude_blocks[i,j][k,l]*percent





        


# =========== 16x16 block normalization ==============










print("Done")
