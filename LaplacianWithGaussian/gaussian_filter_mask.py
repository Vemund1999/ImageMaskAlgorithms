import cv2
import numpy as np



def apply_gaussian_filter(img, name_output_image):

    # == making the kernel ==
    kernel_size = 3
    sigma = 1

    # Initilizing a kernel matrix of size 3x3
    kernel = np.zeros((kernel_size, kernel_size), dtype=np.float32)
    # Refering to the center-pixel of the kernel-matrix
    center = (kernel_size - 1) / 2

    # Creating the normaliation factor which will be applied to the gaussian kernel
    norm = 1 / (2*np.pi*sigma**2) 

    # Looping the kernel an applying the normalization
    for i in range(kernel_size):
        for j in range(kernel_size):
            x, y = i - center, j - center
            kernel[i, j] = norm * np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Puts zeros around the border of the image
    padded_img = np.pad(img, ((kernel_size//2, kernel_size//2), (kernel_size//2, kernel_size//2)), mode='constant')
    # Getting the dimensions of the image
    rows, cols = img.shape
    # Initialize the output image
    output = np.zeros_like(img, dtype=np.float32)

    # Applying the kernel over the image
    for i in range(rows):
        for j in range(cols):
            roi = padded_img[i:i+kernel_size, j:j+kernel_size]
            output[i, j] = np.sum(roi * kernel)

    # Normelizing the values
    img = ((img - np.min(img)) / (np.max(img) - np.min(img))) * 255
    img = img.astype(np.uint8)

    cv2.imwrite(name_output_image, output)


