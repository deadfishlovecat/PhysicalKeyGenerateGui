__author__ = 'caocongcong'
import serial
import serial.tools.list_ports
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

if __name__ == "__main__":
    uart_test = uart_communicate()
    send_data = [0, 1, 0, 1, 0, 1, 0, 1]
    uart_test.send_data(send_data)
    uart_test.receive()
    print(uart_test.receive_data)