__author__ = 'caocongcong'
import matplotlib.pyplot as plt
from  Tools.changeFile import  change_to_list

# 绘制原始的RSSI
def draw_rssi(master, slave):
    '''
    :param master: 上位机的RSSI的数据
    :param slave: 下位机的RSSI数据
    :return:
    '''
    plt.figure()
    plt.plot(master, "-g*")
    plt.hold
    plt.plot(slave, "-r+")
    plt.xlabel("the number of frame")
    plt.ylabel("the value RSSI")
    # plt.legend('Alice', 'Bob')
    plt.title("primary data")
    plt.show()

def draw_key(master_key, slave_key):
    '''
    绘制密钥
    :param master_key:上位机生成的密钥
    :param slave_key: 下位机生成的密钥
    :return:
    '''
    plt.figure()
    plt.plot(master_key, "-g*")
    plt.hold
    plt.plot(slave_key, "-r+")
    plt.xlabel("the number of key value")
    plt.ylabel("the value key")
    # plt.legend('Alice', 'Bob')
    plt.title("key value")
    plt.show()

if __name__ == "__main__":
    master, slave = change_to_list('../data/20180713_1511.txt')
    draw_rssi(master, slave)