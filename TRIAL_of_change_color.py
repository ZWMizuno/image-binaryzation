import cv2
import numpy as np

img2 = cv2.imread('temperature/animation-temperature_0000.jpeg')
img_hsv=cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

# lower mask (0-10)
lower_red = np.array([0,20,20])
upper_red = np.array([100,255,255])
mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

# upper mask (170-180)
lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

# join my masks
mask = mask0 + mask1

output_img = img2.copy()
output_img[np.where(mask0!=0)] = [0, 250, 250]

cv2.imshow("output_image", output_img)
cv2.waitKey(0)