__author__ = 'caocongcong'
from Uart.get_com import get_com_by_input
from  Uart.uart import uart_communicate
'''
 进行串口测试——配合RX使用
 测试流程-
        1 使用串口发送数据

        2 等待串口接受的数据
'''
if __name__ == "__main__":
    used_com = get_com_by_input()
    uart_test = uart_communicate(used_com)
    i = 1
    while i > 0:
        data = uart_test.receive()
        print(data)
        uart_test.send_data(data)