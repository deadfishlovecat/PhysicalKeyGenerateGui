__author__ = 'caocongcong'

class constValue():
    '''
    保存一些常量
    '''

    # 数据帧的总数
    frame_length = 255

    # 交织的阶数
    interleave_order = 20

    #平滑的阶数
    smooth_order = 7

    #Rank的阶数
    rank_order = 10

    #双门限量化的系数
    doubleq_Fac = 0.9

    # zigbee一次传输的数据
    translate_once = 60


    # 进行纠错编码的时候一次能传输的数据
    error_translate_once = 190