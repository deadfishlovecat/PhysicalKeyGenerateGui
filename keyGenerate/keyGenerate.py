__author__ = 'cao'
from Uart.uart import uart_communicate
'''
实现数据处理类
'''
class generate_key():
    # 传入的参数为串口的端口号
    def __init__(self, com):
        uart_commu = uart_communicate(com)
        self.primary_rssi_data = uart_commu.uart_get_rssi_data()

