import os
from fire_area import fire_area

def data_to_text(src, dst):
    '''
    数据读入，提取，写入
    src: 存放图片的文件夹
    dst: 数据存放的路径
    return: None
    '''
    txt = []
    filenames = os.listdir(src)
    filenames.sort(key= lambda x:(int((x.split('_')[1]).split('.')[0]))) # train_2045.png
    #filenames.sort(key=lambda x: int(x.split('.')[0]))  # 2045.png
    # print(filenames)
    for item in filenames:
        if item.endswith('.jpeg'):
            area = fire_area('temperature/'+ item) # 不加'temperature/'读不到temperature文件夹中的图片，只会在本目录读字符
            txt.append(area)

    with open(dst, 'w') as fo:
        for item in txt:
            fo.write(str(item) + '\n')