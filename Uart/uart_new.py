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
        primary_rssi_data = []
        self.rssi_data = []
        for i in range(constValue.frame_length*3):
            primary_rssi_data.append(int.from_bytes(self.ser.read(), byteorder="big"))
        for i in range(constValue.frame_length):
            data = primary_rssi_data[i*3+2] - ord('0')
            data += (primary_rssi_data[i*3+1] - ord('0'))*10
            self.rssi_data.append(data)

    # 发送数据
    def send_data(self, data):
        length = len(data)
        self.ser.write(bytes([length]))
        for i in range(len(data)):
            self.ser.write(bytes([data[i]]))



    # 接收数据
    def receive(self):
        self.receive_data = []
        data_length = int.from_bytes(self.ser.read(), byteorder="big")
        for i in range(data_length):
            self.receive_data.append(int.from_bytes(self.ser.read(), byteorder="big"))

        return self.receive_data


    def send_end(self):
        data = [1, 1]
        self.send_data(data)

    # 关闭串口
    def close(self):
        self.close()

    def get_ack(self):
        ack = int.from_bytes(self.ser.read(), byteorder="big")
        if (ack == 1):
            return True
        else:
            return False
if __name__ == "__main__":
    used_com = get_com_by_input()
    uart_test = uart_communicate(used_com)
    send_data = [0, 1, 0, 1, 0, 1, 0, 1]
    uart_test.send_data(send_data)
    uart_test.receive()
    print(uart_test.receive_data)