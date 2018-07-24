__author__ = 'caocongcong'
import serial
import time
import serial.tools.list_ports
from tools.changeFile import change_to_list
from keyGenerate.draw import draw_rssi, draw_key
import keyGenerate.dealData as deal
from keyGenerate.Error_correction import encode, decode, delete_value
from tools.ConstValue import constValue

from keyGenerate.main import get_key_final

def split_data( data_input ):
    need_len = 255
    master_data = []
    slave_data = []
    for i in range(need_len):
        # 暴力写
        # str_data = primary_data[(i*3):(i+1)*3]
        # str_data = str_data.replace(":", "10")
        # str_data = str_data.replace(";", "11")
        # slave_data.append(int(str_data))
        str_data = data_input[(i*3)+2]
        data = ord(str_data) - ord('0')
        str_data = data_input[(i*3)+1]
        data += (ord(str_data) - ord('0'))*10
        slave_data.append(-data)

    label = data_input[(need_len * 3): (need_len*3+7)]

    for i in range(need_len):
        # 暴力写
        # str_data = primary_data[(i*3)+need_len*3+7:(i+1)*3+need_len*3+7]
        # str_data = str_data.replace(":", "10")
        # str_data = str_data.replace(";", "11")
        # master_data.append(int(str_data))
        str_data = data_input[(i*3)+2+need_len*3+7]
        data = ord(str_data) - ord('0')
        str_data = data_input[(i*3)+1++need_len*3+7]
        data += (ord(str_data) - ord('0'))*10
        master_data.append(-data)

    return master_data, slave_data


def deal_data(primary_master_data, primary_slave_data):
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
    print(delete_index)
    master_key = delete_value(master_key, delete_index)
    slave_key = delete_value(slave_key, delete_index)
    draw_key(master_key, slave_key)
# 获取所有的数据
if  __name__ == "__main__":
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) <= 0:
        print("The Serial port can't find!")
    else:
        for port in port_list:
            print(port)

    used_port = input("输入串口号:\n")
    try:
        ser = serial.Serial(used_port, 38400)
    except:
        print("开启串口失败")
    else:
        print("串口初始化成功")
    data = []
    while len(data) < 1537:
        read_data = ser.read()
        data.append(read_data)

    print(len(data))

    master_data, slave_data = split_data(data)
    deal_data(master_data, slave_data)

