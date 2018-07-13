__author__ = 'caocongcong'

def change_file(path):
    '''
    将接受到数据文件进行拆分，得到两个文件分别叫做master和slave
    :return:
    '''
    slave_data = []
    master_data = []
    need_len = 255
    with open(path, 'r') as f:
        primary_data = f.read()

    for i in range(need_len):
        str_data = primary_data[(i*3):(i+1)*3]
        slave_data.append(int(str_data))

    label = primary_data[(need_len * 3): (need_len*3+7)]
    print(label)

    for i in range(need_len):
        str_data = primary_data[(i*3)+need_len*3+7:(i+1)*3+need_len*3+7]
        master_data.append(int(str_data))

    with open('../data/slave.txt', 'w') as f:
        for data in slave_data:
            f.write(str(data)+" ")
    f.close()

    with open('../data/master.txt', 'w') as f:
        for data in master_data:
            f.write(str(data)+" ")
    f.close()
if __name__ == "__main__":
    change_file('../data/20180713.txt')

