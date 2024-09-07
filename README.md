# COLOR_CONVERSIONS_OF-IMAGE
## AIM
Write a Python program using OpenCV that performs the following tasks:

i) Read and Display an Image.

ii) 	Draw Shapes and Add Text.

iii) Image Color Conversion.

iv) Access and Manipulate Image Pixels.

v) Image Resizing

vi) Image Cropping

vii) Image Flipping

viii)	Write and Save the Modified Image


## Software Required:
Anaconda - Python 3.7
## Algorithm:
### Step1:
Load an image from your local directory and display it.
### Step2:
o	Draw a line from the top-left to the bottom-right of the image.
o	Draw a circle at the center of the image.
o	Draw a rectangle around a specific region of interest in the image.
o	Add the text "OpenCV Drawing" at the top-left corner of the image.

### Step3:
o	Convert the image from RGB to HSV and display it.
o	Convert the image from RGB to GRAY and display it.
o	Convert the image from RGB to YCrCb and display it.
o	Convert the HSV image back to RGB and display it.

### Step4:
o	Access and print the value of the pixel at coordinates (100, 100).
o	Modify the color of the pixel at (200, 200) to white.

### Step5:
o	Resize the original image to half its size and display it.
### Step6:
o	Crop a region of interest (ROI) from the image (e.g., a 100x100 pixel area starting at (50, 50)) and display it.
### Step7:
o	Flip the original image horizontally and display it.
o	Flip the original image vertically and display it.

### Step8:
o	Save the final modified image to your local directory.
<hr>

### Program:
### Developed By: SARAVANA KUMAR M
### Register Number: 212222230133
### i)Read and Display an Image
```
import cv2 img1=cv2.imread("me.jpg")
if img1 is None:
    print("Error: Image not loaded.")
else:
    img1 = cv2.resize(img1, (1100, 720))
cv2.imshow('Saravana kumar',img1)
cv2.waitKey(0)
cv2.destroyallwindows
```

### ii)Draw Shapes and Add Text

#### drawing line
```
height, width, _ = img1.shape
image1 = cv2.line(img1, (0, 0), (width, height), (0, 255, 0), thickness=5) 
cv2.imshow('saravana kumar', image1)
cv2.waitKey(0) 
cv2.destroyAllWindows()
```
 
#### drawing circle at center
```
height, width, _ = img1.shape
center = (width // 2, height // 2) 
radius = 50
image1 = cv2.circle(img1, center, radius, (0, 255, 0), thickness=5) 
cv2.imshow('saravana kumar', image1)
cv2.waitKey(0) 
cv2.destroyAllWindows()
```
#### drawing rectangle
```
image1 = cv2.rectangle(img1, (100, 100), (300, 300), (255, 0, 0), thickness=5)
cv2.imshow('saravana kumar', image1)
cv2.waitKey(0) 
cv2.destroyAllWindows()
```
#### Add text in image
```
text = "OpenCV Drawing" 
position = (10, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (0, 0, 0)
thickness = 2
image1 = cv2.putText(img1, text, position, font, font_scale, color, thickness)
cv2.imshow('saravana kumar', image1)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
```

### iii)Image Color Conversion

#### RGB to HSV and GRAY
```
img2 = cv2.resize(img1,(400,300)) 
cv2.imshow('Original Image',img2)
hsv2= cv2.cvtColor(img2,cv2.COLOR_RBG2HSV) cv2.imshow('RGB2HSV',hsv2)
gray2= cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY) cv2.imshow('RGB2GRAY',gray2)

cv2.waitKey(0) 
cv2.destroyAllWindows() 
```

#### HSV to RGB:
```
img2 = cv2.resize(img1,(400,300)) 
cv2.imshow('Original Image',img2)

hsv_img = cv2.cvtColor(img2, cv2.COLOR_RGB2HSV) 
cv2.imshow('RGB2HSV',hsv_img)
cv2.imshow('RGB from HSV Image', rgb_from_hsv_img)
cv2.waitKey(0) cv2.destroyAllWindows()
```
#### RGBto YCrCb:
```
img2 = cv2.resize(img1,(400,300)) 
cv2.imshow('Original Image',img2)

YCrCb1= cv2.cvtColor(img2, cv2.COLOR_RGB2YCrCb) 
cv2.imshow('RGB-2-YCrCb',YCrCb1)
cv2.waitKey(0) 
cv2.destroyAllWindows()
```
### iv)Access and Manipulate Image Pixels
```
pixel_value = img[100, 100]
print(f"Pixel value at (100, 100): {pixel_value}")
img[200, 200] = [255, 255, 255]
cv2.imwrite('modified_image.jpg', img)
cv2.imshow("saravana kumar",img)
cv2.waitKey(0)
```

### v)Image Resizing
```
height, width,_ = img.shape
resized_img = cv2.resize(img, (width // 2, height // 2))
cv2.imshow('Resized Image', resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

### vi)Image Cropping
```
roi = img[50:150, 50:150]

cv2.imshow('Cropped ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### vii)Image Flipping
```
flipped_horizontally = cv2.flip(img, 1)
flipped_vertically = cv2.flip(img, 0)
cv2.imshow('Horizontally Flipped Image', flipped_horizontally)
cv2.waitKey(0)
cv2.imshow('Vertically Flipped Image', flipped_vertically)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### viii)Write and Save the Modified Image
```
flipped_vertically = cv2.flip(img, 0)
cv2.imwrite('flipped_vertically.jpg', flipped_vertically)
print("Images saved successfully!")
```
<hr>

## Output:

### i)Read and Display an Image

![Screenshot 2024-09-05 161804](https://github.com/user-attachments/assets/a79a79cb-11e7-4671-955c-14f6242f795a)

### ii)Draw Shapes and Add Text
#### drawing line

![Screenshot 2024-09-07 161245](https://github.com/user-attachments/assets/425d9aa8-5b61-4dcb-89ec-563402c71ab5)

#### drawing circle at center
![Screenshot 2024-09-07 161744](https://github.com/user-attachments/assets/e3cf78da-610f-4e40-985f-95cf5df6bd26)

#### drawing rectangle
![Screenshot 2024-09-07 161831](https://github.com/user-attachments/assets/e6bc3c66-43f0-4243-b3d7-b1e6ddc1c665)

#### Add text in image
![Screenshot 2024-09-07 161918](https://github.com/user-attachments/assets/f9b5f8fa-14a6-4ad0-8ecf-5071f852b8ec)


### iii)Image Color Conversion

#### RGB to HSV and GRAY
![Screenshot 2024-09-07 162003](https://github.com/user-attachments/assets/d7ebd5b6-19de-46be-afca-f38374e60ad8)

#### HSV to RGB:
![Screenshot 2024-09-07 162204](https://github.com/user-attachments/assets/4dd009bd-7d99-40be-bc88-50448e0327c1)

#### RGBto YCrCb:
![Screenshot 2024-09-07 162243](https://github.com/user-attachments/assets/c88f16ce-1a5b-4444-beba-f4f355cbb478)

### iv)Access and Manipulate Image Pixels
![Screenshot 2024-09-07 162705](https://github.com/user-attachments/assets/39fc2ccc-5b5f-45fe-a9e4-686d9bbb17f7)

![image](https://github.com/user-attachments/assets/663d3b2c-7fc5-4ac8-9bb1-d8167902e524)


### v)Image Resizing
![Screenshot 2024-09-07 163111](https://github.com/user-attachments/assets/8298987f-8644-4038-bb0e-8fc38c832f42)


### vi)Image Cropping
![Screenshot 2024-09-07 163406](https://github.com/user-attachments/assets/11b42df7-b170-48b3-b8a6-f2cf2c8f0356)

### vii)Image Flipping
![Screenshot 2024-09-07 163633](https://github.com/user-attachments/assets/a4750738-074b-44b6-b98c-9f1fb8fa0708)

### viii)Write and Save the Modified Image
![image](https://github.com/user-attachments/assets/dc5dd778-bb82-413f-9c64-26f1d9ce415a)



## Result:
Thus the images are read, displayed, and written ,and color conversion was performed  successfully using the python program.







