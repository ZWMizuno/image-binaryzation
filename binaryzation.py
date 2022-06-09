import cv2

image = cv2.imread('temperature/animation-temperature_0000.jpeg')  # 读入图片
cropped_image = image[115:615, 412:613] # Slicing to crop the image
crop_gray = cv2.cvtColor(cropped_image, cv2.COLOR_RGB2GRAY)  # 二值化函数

cv2.threshold(cropped_image, 160, 255, 0, cropped_image)  # 二值化函数

cv2.imshow("cropped_image", cropped_image)  # 图片显示

cv2.waitKey(0)
#cv2.imwrite('two_result.jpg', image)  # 保存当前灰度值处理过后的文件

# 图像的二值化，就是将图像上的像素点的灰度值设置为0或255，也就是将整个图像呈现出明显的只有黑和白的视觉效果。
# 一幅图像包括目标物体、背景还有噪声，要想从多值的数字图像中直接提取出目标物体，常用的方法就是设定一个阈值T，用T将图像的数据分成两部分：大于T的像素群和小于T的像素群。这是研究灰度变换的最特殊的方法，称为图像的二值化（Binarization）。

# Python-OpenCV中提供了阈值（threshold）函数：
# cv2.threshold（）
# 函数：
# 1. src 指原图像，原图像应该是灰度图。
# 2. x 指用来对像素值进行分类的阈值。
# 3. y 指当像素值高于（有时是小于）阈值时应该被赋予的新的像素值
# 4. Methods 指不同的阈值方法，