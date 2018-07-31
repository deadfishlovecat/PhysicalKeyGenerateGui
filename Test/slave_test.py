__author__ = 'caocongcong'
from keyGenerate.keyGenerate import generate_key
from Uart.get_com import get_com_by_input

# 与RX相连
if __name__ == "__main__":
    com = get_com_by_input()
    keyGenerate_test = generate_key(com)
    i = 1
    while i > 0:
        data = keyGenerate_test.uart_commu.receive()
        print(data)
        keyGenerate_test.uart_commu.send_data(data)
    # keyGenerate_test.get_key_slave()
    # print(keyGenerate_test.key)