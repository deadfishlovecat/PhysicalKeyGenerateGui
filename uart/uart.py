__author__ = 'caocongcong'
import serial
from tools.ConstValue import constValue

# 使用串口接受RSII的数据，长度为255

class uart_communicate():
    def __init__(self):
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) <= 0:
            print("The Serial port can't find!")
        else:
            for port in port_list:
            print(port)

        used_port = input("输入串口号:\n")
        try:
            self.ser = serial.Serial(used_port, 38400)
        except:
            print("开启串口失败")
        else:
            print("串口初始化成功")

    ## 获取RSSI数据
    def uart_get_rssi_data(self):
        self.rssi_data = []
        while len(self.rssi_data) < constValue.frame_length * 3:
            read_data = self.ser.read()
            self.rssi_data.append(read_data)


    # 发送数据
    def send(data):
        pass

    # 接受数据