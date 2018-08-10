__author__ = 'caocongcong'
# 密钥生成中的处理处理函数
import math

def interleave(data, m):
    '''
    进行数据交织，
    :param data: 原始数据
    :param m:
    :return result: 交织后的结果
    '''
    result = []
    data_length = len(data)
    # 余数
    remainder = data_length % m
    # 商
    quo = int(data_length / m)

    for i in range(m):
        if i < remainder:
            for j in range(quo+1):
                result.append(data[i + j*m])
        else:
            for j in range(quo):
                result.append(data[i+j*m])

    return result


def smooth(data, SPAN):
    '''
    进行平滑操作
    :param data:数据
    :param m: 阶数
    :return:平滑后的数据
    '''
    data_length = len(data)
    result = []
    n = 0
    if SPAN % 2 == 1:
        n = (SPAN-1)/2
    else:
        n = (SPAN-2)/2

    for i in range(data_length):
        pn = n
        if i < n:
            pn = i
        elif (data_length - 1 - i) < n:
            pn = data_length - i - 1
        data_sum = 0.0
        for j in range(int(i-pn), int(i+pn)+1):
            data_sum += data[j]
        # print(int((data_sum/(2*pn+1))*10000))
        result.append(int(int((data_sum/(2*pn+1))*10000)/10000))
    return result

def Rank(data, K):
    '''
    进行信息调和
    :param data:原始数据
    :param m:阶数
    :return:调和后的数据
    '''
    tmp_sum = 1.0
    data_length = len(data)
    result =  [0] * data_length
    for i in range(int(data_length/K)):
        for j in range(K):
            for s in range(K):
                if (i*K+j != i*K+s):
                    if (data[i*K+j] > data[i*K+s]):
                        tmp_sum += 1.0
                    if (abs(data[i*K+j] - data[i*K+s]) == 0):
                        tmp_sum += 0.5
            result[i*K+j] = tmp_sum
            tmp_sum = 1.0
    return result

def doubleq(data, fac):
    '''
    进行双门限量化
    :param data:
    :param rate:
    :return:返回生成的01bit和需要删除的index
    '''
    # 计算均值
    sum_value = sum(data)
    mean_value = sum_value/len(data)

    # 计算标准差
    sum_value = 0.0
    for i in range(len(data)):
        sum_value += (data[i] - mean_value)*(data[i] - mean_value)
    std_value = math.sqrt(sum_value / (len(data) - 1))

    # 计算上下门限
    value_up = mean_value + fac * std_value
    value_down = mean_value - fac * std_value

    # 进行量化
    # 需要的删除的index
    delete_index = []
    # 量化后的bits
    result_bits = []

    for i in range(len(data)):
        # 在上下门限之间,删除
        if data[i] <= value_up and data[i] >= value_down:
            delete_index.append(i)

            # -1 表示无效位
            result_bits.append(-1)
        # 大于上限
        elif data[i] > value_up:
            result_bits.append(1)
        # 低于下限
        else:
            result_bits.append(0)
    return result_bits, delete_index

def codeGen(q_data, delete_index_master, delete_index_slave):
    '''
    进行密钥生成
    :param q_data: 量化后的数据
    :param delete_index_master: 上位机需要删除的index
    :param delete_index_slave: 下位机需要删除的index
    :param smooth_data: 平滑后的数据
    :return: code_result 生成的密钥 delete_index 原始数据中删除的index
    '''
    code_result = []
    delete_index = []
    for i in range(len(q_data)):
        if (not i in delete_index_master) and (not i in delete_index_slave):
            code_result.append(q_data[i])
        else:
            delete_index.append(i)
    return code_result, delete_index

# 将primary_data中index的元素全部提取出来
def get_new_rssi(primary_data, index):
    result = []
    for i in range(len(index)):
        result.append(primary_data[index[i]])
    return result


if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    data1 = [1,2,3,4]
    data2 = [2,5,6,7]
    print(get_new_rssi(data, data1, data2))

