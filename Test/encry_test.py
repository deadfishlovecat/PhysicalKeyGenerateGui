__author__ = 'caocongcong'

# 加密函数，参数位密钥和数据
def encry(key, data):
    encry_data = []
    for i in range(len(data)):
        tmp = data[i] ^ key[i % len(key)]
        encry_data.append(tmp)

# 解密函数，参数位密钥和加密后的数据
def decry(key, encry_data):
    result = []
    for i in range(len(encry_data)):
        tmp = encry_data[i] ^ key[i % len(key)]
        result.append(result)

def check(data1, data2):
    if len(data2) != len(data1):
        return False
    for i in len(data1):
        if data1[i] != data2[i]:
            return False
    return True


if __name__ == "__main__":
    data_len = 1000
    key_len = 60
