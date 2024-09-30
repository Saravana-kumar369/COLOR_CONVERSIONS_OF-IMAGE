import cv2
import numpy as np
from google.colab.patches import cv2_imshow  # For displaying images in Google Colab

# Read and display image
image = cv2.imread("IMAGE2.webp")
cv2_imshow(image)

# Write an image
original_output_path = "original_image.jpg"
cv2.imwrite(original_output_path, image)
print(f"Original image saved to: {original_output_path}")

# Read the saved image
saved_image = cv2.imread(original_output_path)

# Display the saved image
cv2_imshow(saved_image)

# Save the saved image to a new file
new_output_path = "new_saved_image.jpg"
cv2.imwrite(new_output_path, saved_image)
print(f"Saved image saved to: {new_output_path}")

# ACCESSING ROWS AND COLUMNS
# Get the shape of the image (rows, columns, channels)
rows, columns, channels = image.shape
print(f"Image Shape: Rows={rows}, Columns={columns}, Channels={channels}")

# Assign random values to pixels in the first row and first column
image[0, :] = np.random.randint(0, 256, size=(columns, channels))  # Random values for the first row
image[:, 0] = np.random.randint(0, 256, size=(rows, channels))     # Random values for the first column

# Display the modified image
cv2_imshow(image)

# Cut and paste the image
# Display the original image
cv2_imshow(image)

# Define the region to cut (example: top-left corner, width=100, height=100)
cut_region = image[0:100, 0:100]

# Paste the cut region back onto the image (example: paste at (200, 200))
image[200:300, 200:300] = cut_region

# Display the modified image
cv2_imshow(image)

####### COLOR CONVERSION
## Convert BGR and RGB to HSV and GRAY
# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert BGR to HSV
image_hsv_bgr = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Convert RGB to HSV
image_hsv_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)

# Convert BGR to Grayscale
image_gray_bgr = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert RGB to Grayscale
image_gray_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

# Display the images
print("BGR TO GRAY")
cv2_imshow(image_gray_bgr)
print("RGB TO GRAY")
cv2_imshow(image_gray_rgb)

## Convert HSV to RGB and BGR
# Convert HSV to RGB
image_rgb_hsv = cv2.cvtColor(image_hsv_bgr, cv2.COLOR_HSV2RGB)

# Convert HSV to BGR
image_bgr_hsv = cv2.cvtColor(image_hsv_bgr, cv2.COLOR_HSV2BGR)

# Display the RGB image (HSV to RGB)
print("HSV TO RGB")
cv2_imshow(image_rgb_hsv)

# Convert RGB and BGR to YCrCb
# Convert BGR to YCrCb
image_ycrcb_bgr = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Convert RGB to YCrCb
image_ycrcb_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)

# Display the original BGR image
cv2_imshow(image)

# Display the YCrCb images
print("YCrCb from BGR")
cv2_imshow(image_ycrcb_bgr)
print("YCrCb from RGB")
cv2_imshow(image_ycrcb_rgb)

# Split and Merge RGB Image
# Split the RGB channels
blue_channel, green_channel, red_channel = cv2.split(image)

# Display the individual RGB channels
print("BLUE CHANNEL")
cv2_imshow(blue_channel)
print("GREEN CHANNEL")
cv2_imshow(green_channel)
print("RED CHANNEL")
cv2_imshow(red_channel)

# Merge the RGB channels back together
merged_image = cv2.merge([blue_channel, green_channel, red_channel])

# Display the merged image
cv2_imshow(merged_image)

## Split and merge HSV Image
# Convert BGR to HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Split the HSV channels
hue_channel, saturation_channel, value_channel = cv2.split(image_hsv)

# Display the original BGR and HSV images
print("ORIGINAL IMAGE")
cv2_imshow(image)
print("HSV IMAGE")
cv2_imshow(image_hsv)

# Display the individual HSV channels
print("HUE CHANNEL")
cv2_imshow(hue_channel)
print("SATURATION CHANNEL")
cv2_imshow(saturation_channel)
print("VALUE CHANNEL")
cv2_imshow(value_channel)
