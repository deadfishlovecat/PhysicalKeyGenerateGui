__author__ = 'cao'

import serial.tools.list_ports

def get_com_by_input():
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) <= 0:
        print("The Serial port can't find!")
    else:
        for port in port_list:
            print(port)
    used_port = input("输入串口号:\n")
    return used_port