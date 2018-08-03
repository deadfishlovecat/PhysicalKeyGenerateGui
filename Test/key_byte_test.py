__author__ = 'cao'
import random
def get_key_byte(data):
    # if len(data) % 8 != 0:
    #     for i in range(len(data) % 8):
    #         data.pop()
    result = []
    for i in range(int(len(data)/8)):
        tmp_int = change_to_byte(data[i*8:(i+1)*8])
        result.append(tmp_int)
    print(result)

# 将八个byte转化成一个int
def change_to_byte(data):
    result = 0
    for i in range(len(data)):
        result += data[i]*pow(2,i)
    return result
if __name__ == "__main__":
    key = []
    for i in range(255):
        tmp = random.random()
        if tmp > 0.5:
            tmp = 1
        else:
            tmp = 0
        key.append(tmp)

    print(key)
    get_key_byte(key)