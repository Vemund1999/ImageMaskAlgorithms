import skimage
import numpy as np
import sys
from matplotlib import pyplot as plt
from skimage import io,util,color



def Sobel_Filter(im):
    img = im
    io.imsave("Lena-Gray.png",img)
    ###w =2
    out = np.zeros(img.shape, dtype=np.float)
    print("sobel filtering")
    for i in range(1,im.shape[0]-1):
        for j in range(1,im.shape[1]-1):
            dx = (im[i-1,j+1] + 2*im[i,j+1] + im[i+1,j+1]) - (im[i-1,j-1] + 2*im[i,j-1]+ im[i+1,j-1])
            dy = (im[i+1,j-1] + 2*im[i+1,j] +im[i+1,j+1]) - (im[i-1,j-1] + 2*im[i-1,j]+im[i-1,j+1])
            out[i,j] = abs(dx) + abs(dy)

    print(out[i,j])
    return out
def main():
    # Import image using the first command line argument. The image is converted to
    # grayscale before type conversion to float
    image = color.rgb2gray(io.imread(sys.argv[1]))
    #image = np.array(image) * 255
    img_sobel = Sobel_Filter(image)
    print(img_sobel)
    # Save the transformed image to the filename in the 2nd command line argument
    outFile = sys.argv[2]
    io.imsave(outFile, img_sobel)


if __name__== "__main__":
main()
