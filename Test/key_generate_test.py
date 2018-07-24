__author__ = 'cao'
from keyGenerate import keyGenerate
from Uart.get_com import get_com_by_input
if __name__ == "__main__":
    com = get_com_by_input()
    keyGenerate_test = keyGenerate(com)
    print(keyGenerate_test.primary_rssi_data)