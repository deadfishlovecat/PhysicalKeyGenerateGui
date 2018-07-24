__author__ = 'caocongcong'
### 在单片机实现过程中发现程序会出现数据栈溢出，尝试进行原位操作
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