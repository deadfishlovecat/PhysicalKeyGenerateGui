__author__ = 'caocongcong'

# 测试密钥生成
# 与TX相连
from keyGenerate.keyGenerate import generate_key
from Uart.get_com import get_com_by_input

if __name__ == "__main__":
    com = get_com_by_input()
    keyGenerate_test = generate_key(com)
    i = 5
    data = [2, 3, 4, 5, 6, 7, 8, 9]
    keyGenerate_test.get_key_master()
    print(keyGenerate_test.key)