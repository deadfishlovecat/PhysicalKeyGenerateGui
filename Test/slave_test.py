__author__ = 'caocongcong'
from keyGenerate.keyGenerate import generate_key
from Uart.get_com import get_com_by_input
import time

# 与RX相连
if __name__ == "__main__":
    com = get_com_by_input()
    keyGenerate_test = generate_key(com)
    keyGenerate_test.get_key_slave()
    keyGenerate_test.error_correction_slave()
    print(len(keyGenerate_test.key))
    print("发送完毕")
    time.sleep(1)
    data = []
    for i in range(60):
        data.append(i)

    for i in range(10):
        print(i)
        keyGenerate_test.send_data(data)