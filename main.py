from write import data_to_text
from analyse import Mor_plot

txt = 'data.txt' # 数据存放路径
source = 'temperature' # 图片文件夹
image = 'Morphological analysis2.png' # 分析结果图像保存路径
model = 1 # 0 面积/画布   1 周长/面积

data_to_text(source, txt, model) # 读取文件，提取数据，数据处理，数据写入
Mor_plot(txt,image) # 数据分析，保存结果