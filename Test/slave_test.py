__author__ = 'caocongcong'
from keyGenerate.keyGenerate import generate_key
from Uart.get_com import get_com_by_input

# 与RX相连
if __name__ == "__main__":
    com = get_com_by_input()
    keyGenerate_test = generate_key(com)
<<<<<<< HEAD
=======
    i = 1
    while i > 0:
        data = keyGenerate_test.uart_commu.receive()
        print(data)
        keyGenerate_test.uart_commu.send_data(data)
>>>>>>> 5d0bc5fd0ff24b02a7e53faf32e45d0495ce8d85
    # keyGenerate_test.get_key_slave()
    # print(keyGenerate_test.key)