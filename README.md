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





# SVM model to classify digits
I trained an SVM model on the images. I used a penalty


multiplier equal to 1 (C=1),


gaussian kernel (kernel=rbf),

and varied the gamma value between the following values:


param_grid = {'svm__gamma': [0.001, 0.01, 1.0, 10.0

![bilde](https://github.com/user-attachments/assets/6d5b68f9-a767-4b90-b146-a83566f533d2)


I trained the model on the

images without any modification,

after having extracted the HOG features

after having extracted the HOG features and applied PCA to reduce the dimensionality to 500.

These were the results

![bilde](https://github.com/user-attachments/assets/b9180603-f4c8-47b5-ac49-acb3e3107b1c)


The best parameters for gamma were scale in all cases

It can be seen that the accuracy increases when using the HOG features to train the model. The HOG features reduce the noise in an image by being made up of the magnitude and angle of the image. The model is therefore able to find the more important patterns in the data, and more able to classify the images.

It can be seen that the training time for the model increased when training the model on the HOG features. The reason the training time increases is because the dimensionality of the data increases when extracting the HOG features.
Originally the images have a dimensionality of 784 (each image is of size 28x28=782 pixels). After extracting HOG features the dimensionality increases to 1296.

PCA is used in the last run of the model. The model that uses PCA has the lowest running time. The PCA decreases the data dimensionality by combining groups of highly correlated data, into principal components, which are the new combined data points.

PCA is good to use because it reduces the dimensionality of the data, which means training time decreases, but it also manages to keep the accuracy despite leaving some data out in the dimensionality reduction. The accuracy might decrease if too much information is lost in the dimensionality reduction, or increase if the noise in the data is reduced.








