__author__ = 'caocongcong'
import numpy as np
import random
def inter(primary_data_input):
    '''
    对原始数据进行交织
    :param primary_data: 类型为list,为删除后的01比特密钥
    :return:
    '''

    # 首先补全成4的倍数
    primary_data = primary_data_input.copy()
    if len(primary_data) % 4 != 0:
        add_len = 4 - (len(primary_data) % 4)
        for i in range(add_len):
            primary_data.append(0)

    # 转化成numpy
    numpy_primary_data = np.array(primary_data)
    numpy_primary_data = numpy_primary_data.reshape((4, -1))

    # 返回结果
    return numpy_primary_data

def haming_encode(data):
    '''
    完成汉明编码，编码方式为74汉明码a
    :param data 为一个长度为4的list, 顺序分别为 a6 a5 a4 a3
    :return: 返回一个长度为3的list, 分别为 a2 a1 a0
    '''

    a6 = data[0]
    a5 = data[1]
    a4 = data[2]
    a3 = data[3]
    a2 = a6 ^ a4 ^ a3
    a1 = a6 ^ a5 ^ a4
    a0 = a5 ^ a4 ^ a3
    result = []
    result.append(a2)
    result.append(a1)
    result.append(a0)
    return result

def haming_decode(data, code_data):
    '''
    完成汉明解码,编码方式为7 4 汉明编码
    :param data:原始数据，类型为lsit, 顺序分别为 a6 a5 a4 a3
    :param code_data:编码结果数据，类型为list, 分别为 a2 a1 a0
    :return: 如果没有错误就返回true 否则返回false
    '''
    current_code_result = haming_encode(data)
    # 比较每个位置是否相同
    right_flag = True
    for i in range(len(code_data)):
        if code_data[i] == current_code_result[i]:
            continue
        else:
            right_flag = False
            break
    return right_flag



def decode(primary_data, encode_data):
    '''
    进行检错，将不一样的数据都删除
    :param encode_data: 传进来的编码数据
    :param primary_data:原始数据
    :return:  delete_index 需要删除的下标
    '''
    current_encode_data = encode(primary_data)

    loop = int(len(primary_data) / 4)
    print("loop的长度：", loop)
    delete_index = []
    for i in range(0, loop):
        flag = True
        for j in range(0, 3):

            if encode_data[j + i * 3] == current_encode_data[j + i * 3]:
                continue
            else:
                flag = False
                break
        # 说明这个四个需要被删除
        if not flag:
            delete_index.append(i)
            delete_index.append(i+loop)
            delete_index.append(i+loop*2)
            # if (i + loop * 3) < len(primary_data):
            #     delete_index.append(i+loop*3)
    return delete_value(primary_data, delete_index)

def encode(primary_code):
    '''
    分组并依次调用汉明编码
    :param primary_code: 原始的hanming编码
    :return:
    '''
    numpy_data = inter(primary_code)
    result = []
    for i in range(len(numpy_data[0])):
        tmp_list = []
        for j in range(4):
            tmp_list.append(numpy_data[j][i])

        # 调用hanming编码
        tmp_hanming = haming_encode(tmp_list)
        result.extend(tmp_hanming)

    return result

def delete_value(data, index):
    '''
    删除一部分的值
    :param data: 原始的数据
    :param index: 需要删除的下标
    :return: 删除后的值
    '''
    result = []
    for i in range(len(data)):
        if i in index:
            continue
        else:
            result.append(data[i])
    return result


if __name__ == "__main__":
    ## 随机生成255个一样的数据，进行纠错
    data = []
    data2 = []

    for i in range(255):
        tmp = random.uniform(0, 1)
        if tmp > 0.5:
            tmp = 1
        else:
            tmp = 0
        data.append(tmp)
        data2.append(tmp)
    data2[50] = 1
    data2[45] = 1
    data2[32] = 1
    data2[100] =1
    data2[101] =1
    data2[102]= 1
    encode_result = encode(data)
    delete_index = decode(data2, encode_result)
    print(delete_index)
    print(delete_value(data, delete_index))
    print(delete_value(data2, delete_index))
