# COLOR_CONVERSIONS_OF-IMAGE
## AIM
To write a python program using OpenCV to do the following image manipulations.

i) Read, display, and write an image.

ii) Access the rows and columns in an image.

iii) Cut and paste a small portion of the image.

iv)To perform the color conversion between RGB, BGR, HSV, and YCbCr color models.


## Software Required:
Anaconda - Python 3.7
## Algorithm:
### Step1:
Choose an image and save it as a filename.jpg ,
### Step2:
Use imread(filename, flags) to read the file.
### Step3:
Use imshow(window_name, image) to display the image.
### Step4:
Use imwrite(filename, image) to write the image.
### Step5:
End the program and close the output image windows.
### Step6:
Convert BGR and RGB to HSV and GRAY
### Step7:
Convert HSV to RGB and BGR
### Step8:
Convert RGB and BGR to YCrCb
### Step9:
Split and Merge RGB Image
### Step10:
Split and merge HSV Image

##### Program:
### i) Read and display the image
```
import cv2
img1=cv2.imread("me.jpg")
if img1 is None:
    print("Error: Image not loaded.")
else:
    img1 = cv2.resize(img1, (1100, 720))
cv2.imshow('Saravana kumar',img1)
cv2.waitKey(0)
cv2.destroyallwindows
```
### ii)Write the image
```
cv2.imwrite('me.jpg',img1)
```
### iii)Shape of the Image
```
print(img1.shape)
```
### iv)Access rows and columns
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
#### writing in image
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
### v)Cut and paste portion of image
```
img2 = img1[130:200, 110:190]
img1[110:180, 120:200] = img2
cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### vi) BGR and RGB to HSV and GRAY
```
img2 = cv2.resize(img1,(400,300))
cv2.imshow('Original Image',img2)
hsv1= cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
cv2.imshow('RGB2HSV',hsv1)
hsv2= cv2.cvtColor(img2,cv2.COLOR_RBG2HSV)
cv2.imshow('RGB2HSV',hsv2)
gray= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('RGB2GRAY',gray)
gray2= cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',gray2)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### vii) HSV to RGB and BGR
```
img2 = cv2.resize(img1,(400,300))
cv2.imshow('Original Image',img2)

hsv_img = cv2.cvtColor(img2, cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv_img)
cv2.imshow('RGB from HSV Image', rgb_from_hsv_img)
rgb_from_hsv_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)

hsv_img1 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV',hsv_img1)
cv2.imshow('RGB from HSV Image', bgr_from_hsv_img)
bgr_from_hsv_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
### viii) RGB and BGR to YCrCb
```
img2 = cv2.resize(img1,(400,300))
cv2.imshow('Original Image',img2)

YCrCb1= cv2.cvtColor(img2, cv2.COLOR_RGB2YCrCb)
cv2.imshow('RGB-2-YCrCb',YCrCb1)

YCrC21= cv2.cvtColor(img2, cv2.COLOR_BGR2YCrCb)
cv2.imshow('BGR-2-YCrCb',YCrCb2)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### ix) Split and merge RGB Image
```
red_channel, green_channel, blue_channel = cv2.split(img1)

cv2.imshow("Red Channel", red_channel)
cv2.imshow("Green Channel", green_channel)
cv2.imshow("Blue Channel", blue_channel)

merged = cv2.merge((red_channel,green_channel,blue_channel))
cv2.imshow('Merged RGB image',merged)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
### x) Split and merge HSV Image
```
img1=cv2.cvtColor(img1,cv2.COLOR_RGB2HSV)
H,S,V=cv2.split(img1)
cv2.imshow('Hue',H)
cv2.imshow('Saturation',S)
cv2.imshow('Value',V)
merged = cv2.merge((H,S,V))
cv2.imshow('Merged',merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Developed By: SARAVANA KUMAR M
### Register Number: 212222230133

## Output:

### i) Read and display the image

<br>

![image](https://github.com/user-attachments/assets/959f128b-28a4-42e3-b8e3-37dc362ab269)

<br>

### ii)Write the image

<br>

![image](https://github.com/user-attachments/assets/4f9dce92-27d2-48d2-8e71-f984a31ead7f)

<br>

### iii)Shape of the Image

<br>

![image](https://github.com/user-attachments/assets/4b8ccd76-eaad-40a9-ba86-59d3656ce2f0)

<br>

### iv)Access rows and columns
#### drawing line
<br>

![image](https://github.com/user-attachments/assets/0e8149b4-483b-41f4-8f83-1328c4d6e2a2)

<br>

#### drawing circle at center
<br>

![image](https://github.com/user-attachments/assets/3446bdf7-a79a-4698-bf05-76a8eae67234)

<br>

#### drawing rectangle
<br>

![image](https://github.com/user-attachments/assets/7d916bd8-ffa6-4be7-b774-a6bc04bf0046)

<br>

#### writing in image
<br>

![image](https://github.com/user-attachments/assets/46fab65f-38fc-4b2f-a090-d0bfc068b541)

<br>

### v)Cut and paste portion of image
<br>

![image](https://github.com/user-attachments/assets/f87dc48f-4452-4575-b8e2-6c52492744e2)

<br>

### vi) BGR and RGB to HSV and GRAY
<br>

![image](https://github.com/user-attachments/assets/a42a1cc3-58a4-448b-9da7-96e12f63bb3b)

<br>

### vii) HSV to RGB and BGR
<br>

![image](https://github.com/user-attachments/assets/78965f56-351b-45c3-91aa-89f5c42b26ea)

<br>

![image](https://github.com/user-attachments/assets/90a3e610-90e2-4b3b-9801-9eca08e94ab5)

<br>

### viii) RGB and BGR to YCrCb
<br>

![image](https://github.com/user-attachments/assets/d24bda67-4ad5-4b26-8be7-087f30aa7eac)

<br>

### ix) Split and merge RGB Image
<br>

![image](https://github.com/user-attachments/assets/1c7e5fef-fea2-486d-9352-b7f9fb865f7a)

<br>

![image](https://github.com/user-attachments/assets/5a78b8bf-3abe-4c58-bed4-670ed6402ff6)

<br>

### x) Split and merge HSV Image
<br>

![image](https://github.com/user-attachments/assets/ade562d2-0a84-468f-8077-093064e3faa5)

<br>

![image](https://github.com/user-attachments/assets/b8a6b016-ea0f-4298-8b4d-08457c351ff3)

<br>


## Result:
Thus the images are read, displayed, and written ,and color conversion was performed between RGB, HSV and YCbCr color models successfully using the python program.







