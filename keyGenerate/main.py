__author__ = 'caocongcong'
from Tools.changeFile import change_to_list
from keyGenerate.draw import draw_rssi, draw_key
import keyGenerate.dealData as deal
from keyGenerate.Error_correction import encode, decode, delete_value
from Tools.ConstValue import constValue


def get_key_once(master_data, slave_data):
    '''
    进行一次获取密钥
    :param primary_master_data:主机的数据
    :param primary_slave_data: 从机的数据
    :return:
    '''
    #进行平滑
    master_data_smooth = deal.smooth(master_data, constValue.smooth_order)
    slave_data_smooth = deal.smooth(slave_data, constValue.smooth_order)

    #进行Rank操作
    master_data_rank = deal.Rank(master_data_smooth, constValue.rank_order)
    slave_data_rank = deal.Rank(slave_data_smooth, constValue.rank_order)

    # 进行双门限量化
    master_data_doubleq, delete_index_master = deal.doubleq(master_data_rank, constValue.doubleq_Fac)
    slave_data_doubleq, delete_index_slave = deal.doubleq(slave_data_rank, constValue.doubleq_Fac)

    # 进行密钥生成
    master_key, delete_index = deal.codeGen(master_data_doubleq, delete_index_master, delete_index_slave)
    slave_key, delete_index = deal.codeGen(slave_data_doubleq, delete_index_master, delete_index_slave)

    return master_key, slave_key, delete_index

def get_key_final(master_data, slave_data, tolerate_num):
    '''
    得到最终的密钥，重复调用以得到
    :param master_data:
    :param slave_data:
    :param tolerate_num:
    :return:
    '''
    master_key, slave_key, delete_index = get_key_once(master_data, slave_data)
    while (len(delete_index) > tolerate_num):
        # 取数据
        master_data_tmp = []
        slave_data_tmp = []
        for index in delete_index:
            master_data_tmp.append( master_data[index])
            slave_data_tmp.append(slave_data[index])
        master_key_tmp, slave_key_tmp , delete_index = get_key_once(master_data_tmp, slave_data_tmp)
        master_key.extend(master_key_tmp)
        slave_key.extend(slave_key_tmp)

    return master_key, slave_key


if __name__ == "__main__":
    primary_master_data, primary_slave_data = change_to_list('../data/20180713_1511.txt')

    #绘制一下原始图像
    draw_rssi(primary_master_data, primary_slave_data)

    # 首先进行交织
    master_data = deal.interleave(primary_master_data, constValue.interleave_order)
    slave_data = deal.interleave(primary_slave_data, constValue.interleave_order)

    master_key, slave_key = get_key_final(master_data, slave_data, 10)

    draw_key(master_key, slave_key)

    # 进行纠错
    encode_result = encode(slave_key)
    delete_index = decode(master_key, encode_result)
    master_key = delete_value(master_key, delete_index)
    slave_key = delete_value(slave_key, delete_index)
    draw_key(master_key, slave_key)



