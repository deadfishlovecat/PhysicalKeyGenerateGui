__author__ = 'caocongcong'

from Uart.get_com import get_com_by_input
#from  Uart.uart import uart_communicate
from  Uart.uart_new import uart_communicate
'''
 进行串口测试——配置TX用
 测试流程-
        1 等待串口输欧到的数据

        2 等待回收数据
'''
if __name__ == "__main__":


    used_com = get_com_by_input()
    uart_test = uart_communicate(used_com)
    loop = 1
    data = []
    for i in range(199):
        data.append(i)
    while loop > 0:
        print(loop)
        uart_test.send_data(data)
        print("发送完数据")
        data_rece = uart_test.receive()
        print(data_rece)
        loop -= 1
