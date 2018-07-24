__author__ = 'caocongcong'
import serial
from Tools.ConstValue import constValue
from Uart.get_com import get_com_by_input

# 串口通信类，实现了三个函数，分别为获取RSSI值、发送一串数据和得到一串数据

class uart_communicate():
    def __init__(self, used_port):
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
            self.receive()
            self.rssi_data.extend(self.receive_data)

    # 发送数据
    def send_data(self, data):
        data_len = len(data)
        self.ser.write(bytes(str(data_len),"ascii"))
        for i in range(data_len):
            self.ser.write(bytes(str(data[i]),"ascii"))

    # 接收数据
    def receive(self):
        data_len =  int.from_bytes(self.ser.read(), byteorder='big')
        self.receive_data = []
        for i in range(data_len):
            self.receive_data.append(self.ser.read())
    # 关闭串口
    def close(self):
        self.close()
if __name__ == "__main__":
    used_com = get_com_by_input()
    uart_test = uart_communicate(used_com)
    send_data = [0, 1, 0, 1, 0, 1, 0, 1]
    uart_test.send_data(send_data)
    uart_test.receive()
    print(uart_test.receive_data)