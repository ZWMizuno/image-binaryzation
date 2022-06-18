import cv2
import numpy as np

def fire(src,model=0):
    '''
    提取火焰相对大小
    src: 单张图片文件名
    return: 火焰部分相对大小
    '''

    # 读入图片
    image = cv2.imread(src)

    # 切片
    cropped_image = image[115:615, 412:613] # Slicing to crop the image

    # 转HSV
    img_hsv=cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)

    # 在HSV空间设置mask
    lower_red = np.array([0,20,20])
    upper_red = np.array([90,255,255])
    mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

    # 对cropped_image套上mask的修改
    new_img = cropped_image.copy()
    new_img[np.where(mask0!=0)] = [0, 250, 250] # 设置新颜色

    # 图像二值化
    new_gray_img = cv2.cvtColor(new_img, cv2.COLOR_RGB2GRAY)
    _ , output_img = cv2.threshold(new_gray_img, 170, 255, 0) # 调参

    #计算面积
    fire_area = np.sum(output_img > 125)  # 计算白点个数

    if model == 0:
        # 输出 面积/画布
        size = np.size(output_img)
        proportion = fire_area/size
    elif model == 1:
        # 输出 周长/面积
        imgCanny = cv2.Canny(output_img,150,200)
        fire_perimeter = np.sum(imgCanny>125) # 计算白点个数
        proportion = fire_perimeter / fire_area

    # # 图片显示
    # cv2.imshow("output_img", output_img)
    # cv2.waitKey(0)

    return proportion




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