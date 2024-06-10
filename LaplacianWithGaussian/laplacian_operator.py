import cv2
import numpy as np

def apply_laplacian_filter(img, name_output_image):
    # Initilizing a laplacian kernel 3x3 of 2nd derivative
    laplacian_kernel = np.array([[-1, -1, -1],
                                [-1, 8, -1],
                                [-1, -1, -1]])

    # Initialize the output image
    result = np.zeros_like(img)

    # Getting the dimensions of the image
    height, width = img.shape

    # Applying the laplacian kernel over the image
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # Applying the laplacian kernel
            applied_kernel = np.sum(img[i - 1:i + 2, j - 1:j + 2] * laplacian_kernel)
            # Making values within the range 0 to 255
            result[i, j] = np.clip(applied_kernel, 0, 255)

    result = np.uint8(result)

    cv2.imwrite(name_output_image, result)







