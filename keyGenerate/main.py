__author__ = 'caocongcong'
from tools.changeFile import change_to_list
from keyGenerate.draw import draw_rssi, draw_key
import keyGenerate.dealData as deal
from tools.ConstValue import constValue



if __name__ == "__main__":
    primary_master_data, primary_slave_data = change_to_list('../data/20180713.txt')

    #绘制一下原始图像
    draw_rssi(primary_master_data, primary_slave_data)

    # 首先进行交织
    master_data = deal.interleave(primary_master_data, constValue.interleave_order)
    slave_data = deal.interleave(primary_slave_data, constValue.interleave_order)

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
    print(len(master_key))

    draw_key(master_key, slave_key)

