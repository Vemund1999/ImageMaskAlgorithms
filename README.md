# About this repository
This repository showcases different alogithms for image masks, and what the effect of those image algorithms are.


# Laplacian with gaussian
This is the original image

![bilde](https://github.com/user-attachments/assets/d3d6a27a-38bd-49b9-8477-91a10fc3f178)

After using a gaussian filter with a kernel-size 3 and a sigma-value of 1, I got
this image. It’s slighly blurry

![bilde](https://github.com/user-attachments/assets/d715f7ee-a9cb-47ec-983f-219c33dc9aad)

If I apply the laplacian filter directly on the original image, without using the
gaussian filter, I get this image:

![bilde](https://github.com/user-attachments/assets/2e806fbc-1c56-4c82-bb97-d14c3e6a676f)

If I apply the laplacian filter after using the gaussian filter, I get this image:

![bilde](https://github.com/user-attachments/assets/6505146e-863b-4f51-91ee-e361765ea6e1)

The two images using the laplacian filter - with, and without the gaussian filter
have the following differences:
- The image not using the gaussian filter has a lot more noise in it.
- We can see the many details on the apple and on the twig.
- The image using the gaussian has less details.
- The image not using the gaussian filter is a bit lighter than the image using
the gaussian filter.


The laplacian operator applies a laplacian laplacian kernel on the center pixel.
The laplacian kernel's center-value is multiplied by a higher value than the
surrounding pixels,
then the difference between the center-pixel and the surrounding pixels are
calculated.


If there is little difference between the center-pixel and the surrounding pixels is small, then the resulting output is a high value. 
This means the result is a darker pixel.


If there is a high difference between the center-pixel and the surrounding pixels
is high,
then the resulting output is a small value.
This means the result is a lighter pixel.


Applying the gaussian mask results in the pixels in the image having more
similar values.


This means that when applying the laplacian filter afterwards, the smaller
differences disappears from the original image, so more of higher differences
remains.

So details in the output disappears, while only the major outlines remain.


When using the gaussian filter, the output seems a bit darker compared to only
using the laplacian filter. The output image can be sensitive to the intensity of
the gaussian filter. If the image is too blurry, then the output image can lose too
much information. So one has to be careful with the intensity of the gaussian
filter.




