import cv2
import numpy as np
import math



image_path = 'gray.jpeg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
array_2d = np.array(gray_image)

dfdx = np.zeros_like(array_2d)
dfdy = np.zeros_like(array_2d)
magnitude = np.zeros_like(array_2d)
theta = np.zeros_like(array_2d)




for x in range(0, array_2d.shape[0] - 1):
    for y in range(0, array_2d.shape[1] - 1):
        
        if y == array_2d.shape[1] - 1:
            dfdy[x,y] = array_2d[x+1, y]
        else:
            dfdy[x,y] = abs( array_2d[x+1, y] - array_2d[x, y] )


        if x == array_2d.shape[0] - 1:
            dfdx[x,y] = dfdx[x,y] = array_2d[x, y]
        else:
            dfdx[x,y] = abs( array_2d[x, y] - array_2d[x, y+1] )
        

            
        #some = math.sqrt( (dfdx)**2 + (dfdy)**2 )




def save_image(name, array):
    cv2.imwrite(name, array)

save_image("dfdx.jpg", dfdx)
save_image("dfdy.jpg", dfdy)







