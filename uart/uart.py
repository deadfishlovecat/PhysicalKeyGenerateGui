__author__ = 'caocongcong'
import serial
from Tools.ConstValue import constValue
from Uart.get_com import get_com_by_input

# 串口通信类，实现了三个函数，分别为获取RSSI值、发送一串数据和得到一串数据

class uart_communicate():
    def __init__(self, used_port):
        try:
            self.ser = serial.Serial(used_port, 38400, timeout=0.5)
        except:
            print("开启串口失败")
        else:
            print("串口初始化成功")

    ## 获取RSSI数据
    def uart_get_rssi_data(self):
        tmp_rssi_data = []
        self.rssi_data = []
        while len(tmp_rssi_data) < constValue.frame_length * 3:
            self.receive()
            tmp_rssi_data.extend(self.receive_data)

        for i in range(constValue.frame_length):
            str_data = tmp_rssi_data[(i*3)+2]
            data = ord(str_data) - ord('0')
            str_data = tmp_rssi_data[(i*3)+1]
            data += (ord(str_data) - ord('0'))*10
            self.rssi_data.append(-data)


    # 发送数据
    def send_data(self, data):
        for i in range(len(data)):
            self.ser.write(bytes([data[i]]))


    # 接收数据
    def receive(self):
        self.receive_data = []
        while True:
            rece_data = self.ser.read_all()
            if len(rece_data) > 0:
                self.receive_data = rece_data
                break
        return self.receive_data


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