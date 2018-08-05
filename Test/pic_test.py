__author__ = 'caocongcong'
from PIL import Image
import PIL
import struct
import gzip
import numpy as np

# 把图片转化成120*120的的list
def get_ima_data():
    im = Image.open('../data/seu.png')
    img = im.convert('L')
    img.thumbnail((120, 120))
    img_data = np.array(img)
    img = img.resize((240, 240), PIL.Image.ANTIALIAS)
    # print(img.size)
    img.show()
    img_data = img_data.reshape(-1, 1)
    # print(img_data.shape)
    list_data = []
    for i in range(img_data.shape[0]):
        list_data.append(int(img_data[i]))
        print(str(list_data[i]), end=', ')
    return list_data


def compress():
    pass

# print(img_data)
# img = img.resize((200, 200), PIL.Image.ANTIALIAS)
# print(img.size)
# img.show()
if __name__ == "__main__":
    list_data = get_ima_data()
    # print(list_data[0])
    byte_data = bytes(list_data)
    # print(len(byte_data))
    # compree_data = gzip.compress(byte_data)
    # print(len(compree_data))