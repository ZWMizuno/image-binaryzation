# :camera:image processing 
:grin:记录学习过程

## :large_blue_circle:image-binaryzation
火焰的仿真实验图像中，焰心部位温度高，呈红色，周围环境温度低，呈蓝色，外焰部分温度处于中间值，但颜色较亮，在进行设置阈值的图像二值化处理后，火焰外焰轮廓突出，内部焰心和周围环境都没有被凸显。与预期整个火焰区别于周围环境要求不符，为了在图像二值化时融合局部不连续特征，在图像二值化前先进行变色预处理，利用inRange()在HSV空间设置mask给局部图像（焰心）换色，再进行二值化，达到区分目标区域的作用。
