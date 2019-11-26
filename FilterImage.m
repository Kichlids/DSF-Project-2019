%this loads in the image that we want to test
Image = imread('Images\color_blind_F.png');

%this seperates the different colors
%in the image, specifically the red one
imshow(Image)
title('Original Image')
redchannel = Image(:,:,1)
greenchannel = Image (:, :, 2)
bluechannel = Image (:, :, 3)
figure
imshow(redchannel)
title('Red Channel')

%this applies a gaussian filter to the image
%and makes it slightly blurry
B = imgaussfilt(redchannel, 2)
figure
imshow(B,[])
title('Gaussian Filter')

%this applies a threshold to the image
%so we can isolate the letter
level = .82
Ithresh = imbinarize(B,level)
figure
imshow(Ithresh)
title('Binarized')

%this gets rid of noise in the image
%specifically salt and pepper noise
mf = ones(6, 3)/9;
noise_free = imfilter(Ithresh, mf)
figure
imshow(noise_free)
title('Noise Free')