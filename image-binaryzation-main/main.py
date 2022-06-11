from write import data_to_text
from analyse import Mor_plot

txt = 'data.txt' # 数据存放路径
source = 'temperature' # 图片文件夹
image = 'Morphological analysis.png' # 分析结果图像保存路径

data_to_text(source, txt) # 读取文件，提取数据，数据写入
Mor_plot(txt,image) # 数据分析，保存结果