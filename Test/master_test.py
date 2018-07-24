__author__ = 'caocongcong'

# 测试密钥生成
from keyGenerate.keyGenerate import generate_key
from Uart.get_com import get_com_by_input
if __name__ == "__main__":
    com = get_com_by_input()
    keyGenerate_test = generate_key(com)
    keyGenerate_test.get_key_master()
    print(keyGenerate_test.key)