__author__ = 'caocongcong'

# 测试密钥生成
# 与TX相连
from keyGenerate.keyGenerate import generate_key
from Uart.get_com import get_com_by_input

if __name__ == "__main__":
    com = get_com_by_input()
    keyGenerate_test = generate_key(com)
    keyGenerate_test.get_key_master()
    print("未纠错的秘钥：")
    print(len(keyGenerate_test.key))
    print(keyGenerate_test.key)

    keyGenerate_test.erroe_correction_master()
    #keyGenerate_test.uart_commu.send_end()

    i = 0
    while True:
        print(keyGenerate_test.get_data())
        print(i)
        i += 1