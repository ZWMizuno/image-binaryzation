import cv2

image = cv2.imread('temperature/animation-temperature_0000.jpeg')  # 读入图片

cropped_image = image[115:615, 412:613] # Slicing to crop the image

# Display the cropped image
cv2.imshow("cropped", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

