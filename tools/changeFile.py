__author__ = 'caocongcong'

def change_to_file(path):
    '''
    将接受到数据文件进行拆分，得到两个文件分别叫做master和slave
    :return:
    '''
    master_data, slave_data = change_to_list(path)
    with open('../data/slave.txt', 'w') as f:
        for data in slave_data:
            f.write(str(data)+" ")
    f.close()

    with open('../data/master.txt', 'w') as f:
        for data in master_data:
            f.write(str(data)+" ")
    f.close()

def change_to_list(path):
    slave_data = []
    master_data = []
    need_len = 255
    with open(path, 'r') as f:
        primary_data = f.read()

    for i in range(need_len):
        # 暴力写
        # str_data = primary_data[(i*3):(i+1)*3]
        # str_data = str_data.replace(":", "10")
        # str_data = str_data.replace(";", "11")
        # slave_data.append(int(str_data))
        str_data = primary_data[(i*3)+2]
        data = ord(str_data) - ord('0')
        str_data = primary_data[(i*3)+1]
        data += (ord(str_data) - ord('0'))*10
        slave_data.append(-data)

    label = primary_data[(need_len * 3): (need_len*3+7)]

    for i in range(need_len):
        # 暴力写
        # str_data = primary_data[(i*3)+need_len*3+7:(i+1)*3+need_len*3+7]
        # str_data = str_data.replace(":", "10")
        # str_data = str_data.replace(";", "11")
        # master_data.append(int(str_data))
        str_data = primary_data[(i*3)+2+need_len*3+7]
        data = ord(str_data) - ord('0')
        str_data = primary_data[(i*3)+1++need_len*3+7]
        data += (ord(str_data) - ord('0'))*10
        master_data.append(-data)

    return master_data, slave_data
if __name__ == "__main__":
    change_to_file('../data/20180715_1652.txt')
