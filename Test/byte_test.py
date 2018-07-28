__author__ = 'caocongcong'
if __name__ == "__main__":
    # data = [1, 2, 3, 4, 5]
    # for i in range(len(data)):
    #     print(bytes([data[i]]))
    data = 199
    byte_data = bytes([data])
    print(int.from_bytes(byte_data, byteorder="big"))
