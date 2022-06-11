import matplotlib.pyplot as plt
import numpy as np


def Mor_plot(src,dst):
    '''
    Morphological analysis
    src: 数据存放路径
    dst: 分析结果保存路径
    return: None
    '''
    data = []
    with open(src, 'r') as file:  # 打开文件
        file_data = file.readlines()  # 读取所有行
        for row in file_data:
            string = row.rstrip()  # 切掉readlines()带来的换行
            # tmp_list[-1] = tmp_list[-1].replace('\n',',') #去掉换行符
            data.append(float(string))  # 将每行数据插入data中

    scale = len(data)
    x = np.arange(scale)
    plt.plot(x,data)
    plt.xlabel('time')
    # plt.ylabel('fire area size')
    plt.title('Morphological analysis with time')
    plt.legend(['fire area size'])
    plt.savefig(dst) # 先保存，不然show()完之后就没图了
    plt.show()