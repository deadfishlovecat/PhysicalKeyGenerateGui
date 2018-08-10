__author__ = 'caocongcong'
from Tools.ConstValue import constValue
from  keyGenerate.dealData import interleave, smooth, Rank, doubleq
# 测试使用RSSI进行测试

def check(data, data2):
    if len(data) != len(data2):
        print(len(data))
        print(len(data2))

        return False
    for i in range(len(data)):
        if abs(data[i] - data2[i]) > 0.01:
            print("当前位置：", i)
            return False
    return True
if __name__ == "__main__":
    data = constValue.rssi_data
    inter_data = interleave(data, constValue.interleave_order)
    smooth_data = smooth(inter_data, constValue.smooth_order)
    rank_data = Rank(smooth_data, constValue.rank_order)
    q_data, delete_index = doubleq(rank_data, constValue.doubleq_Fac)
    tmp_data = [2, 3, 8, 9, 13, 14, 15, 16, 22, 25, 26, 27, 28, 29, 33, 34, 35, 38, 39, 42, 46, 47, 48, 52, 53, 54, 55, 59, 61, 65, 66, 67, 68, 72, 73, 74, 78, 79, 80, 81, 84, 85, 86, 87, 91, 92, 93, 94, 97, 98, 99, 100, 103, 104, 105, 106, 107, 113, 116, 117, 118, 120, 124, 125, 126, 129, 130, 131, 132, 133, 136, 137, 138, 142, 143, 144, 146, 150, 151, 152, 155, 156, 157, 159, 163, 164, 168, 169, 170, 171, 172, 175, 176, 177, 181, 182, 183, 184, 185, 187, 188, 189, 190, 194, 195, 201, 202, 203, 206, 210, 212, 213, 214, 215, 218, 219, 220, 221, 224, 225, 226, 227, 231, 236, 237, 242, 243, 246, 247, 248, 249]
    print(check(delete_index, tmp_data))