import cv2
import numpy as np

# Leser grayscale
image_path = 'gray.jpeg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Konverterer til 2d array
array_2d = np.array(gray_image)

# Lager kopy av array, som skal representere en smooth array
grayed_2d = np.zeros_like(array_2d)

# Algoritme for masken
def gray_scale_array(center_i):
    max_value = 0
    min_value = 255
    
    for j in range(0, array_2d.shape[1] - 1):
        value = array_2d[center_i, j]
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    avg = (max_value - min_value) / 2
    
    for j in range(0, array_2d.shape[1] - 1):
        value = array_2d[center_i, j]
        if value < avg:
            grayed_2d[center_i, j] = 0
        elif value >= avg:
            grayed_2d[center_i, j] = 255
    


# Looper hver pixel og legger på masken
for i in range(0, array_2d.shape[0] - 1):
    gray_scale_array(i)





print("Done masking")

# Lager et nytt bilde fra den smoothe arrayen
new_image_path = 'gray_scaled_binary.jpg'
cv2.imwrite(new_image_path, grayed_2d)
print("Done")
