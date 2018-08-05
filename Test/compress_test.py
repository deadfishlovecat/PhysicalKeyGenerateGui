__author__ = 'caocongcong'
from Tools import ConstValue
import gzip
if __name__ == "__main__":
    data = ConstValue.constValue.pic_data
    data = bytes(data)
    print(len(data))
    compree_data = gzip.compress(data)
    print(len(compree_data))
    recovery_data = gzip.decompress(compree_data)
    print(len(recovery_data))
