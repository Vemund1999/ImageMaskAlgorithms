import cv2
import numpy as np

# Leser grayscale
image_path = 'gray_scaled_binary.jpeg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Konverterer til 2d array
array_2d = np.array(gray_image)

# Lager kopy av array, som skal representere en smooth array
grayed_2d = np.zeros_like(array_2d)


compnent_val = 255
components_val = 1

# ================= first scan ==========================
def put_value_in_px_based_on_neighbourhood_and_components(center_i, center_j):
    for i in range(-1, 1):
        for j in range(-1, 1):
            if array_2d[center_i + i, center_j + j] != 255 and array_2d[center_i + i, center_j + j] != 0: # px's val not 255, and not 0
                array_2d[center_i][center_j] = array_2d[center_i + i, center_j + j] # make px's value into existing neigh component
                return
    # center px not neighbouring a component
    components_val += 1 # increase component value
    array_2d[center_i][center_j] = components_val #make component value into increased value (new component)
    

# Loop every pixel
for i in range(0, array_2d.shape[0] - 1):
    for j in range(0, array_2d.shape[1] - 1):
        if array_2d[i, j] != compnent_val: # value is not background
            put_value_in_px_based_on_neighbourhood_and_components(i, j)
        

# ================= second scan ==========================
def connect_components(center_i, center_j):
    smallest_comp = 255
    for i in range(-1, 1):
        for j in range(-1, 1):
            if array_2d[center_i + i][center_j + j] < smallest_comp:
                smallest_comp = array_2d[center_i + i][center_j + j]
    array_2d[center_i][center_j] = smallest_comp


for i in range(0, array_2d.shape[0] - 1):
    for j in range(0, array_2d.shape[1] - 1):
        if array_2d[i, j] != compnent_val: # value is not background       
            connect_components(i, j)

# ================= go over and find amount of connected comps =============
components = []
for i in range(0, array_2d.shape[0] - 1):
    for j in range(0, array_2d.shape[1] - 1):
        if array_2d[i,j] != 255:
            components.add( array_2d[i,j] )

components_set = set(components)
print(components.size())


print("Done")

