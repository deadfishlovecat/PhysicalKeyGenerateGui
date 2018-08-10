__author__ = 'cao'
from Uart.uart_new import uart_communicate
import keyGenerate.dealData as deal
from Tools.ConstValue import constValue
from keyGenerate.Error_correction import encode,decode

'''
实现数据处理类
'''
class generate_key():
    # 传入的参数为串口的端口号
    def __init__(self, com):
        self.uart_commu = uart_communicate(com)
        self.uart_commu.uart_get_rssi_data()
        self.primary_rssi_data = self.uart_commu.rssi_data
        self.rssi_data = deal.interleave(self.primary_rssi_data, constValue.interleave_order)
        self.key = []

    def get_key_slave(self):
        while len(self.rssi_data) > 10:
            # print("当前密钥长度:", len(self.key))
            # print("剩余数据长度", len(self.rssi_data))
            # print("总和长度：", len(self.key ) + len(self.rssi_data))
            # 首先进行平滑
            smooth_data = deal.smooth(self.rssi_data, constValue.smooth_order)

            # 然后进行rank
            rank_data = deal.Rank(smooth_data, constValue.rank_order)

            # 进行双门限量化
            data_doubleq, delete_index = deal.doubleq(rank_data, constValue.doubleq_Fac)
            # print("此次发送的删除index长度:", len(delete_index))
            # print(delete_index)
            # print("准备发送数据")
            # 此处考虑如果delete_inde的长度为0
            if (len(delete_index) == 0):
                self.uart_commu.send_data([255])
            else:
                self.uart_commu.send_data(delete_index)
            # print("发送完数据")
            # print("接受数据")
            delete_index_reve = self.uart_commu.receive()
            # print("接受完数据")
            if len(delete_index_reve) == 1 and delete_index_reve[0] == 255:
                delete_index_reve = []
            # print("此次接受的删除index长度:", len(delete_index))

            tmp_key, tmp_delete = deal.codeGen(data_doubleq, delete_index, delete_index_reve)
            self.key.extend(tmp_key)

            self.rssi_data = deal.get_new_rssi(self.rssi_data, tmp_delete)
        print("密钥长度:", len(self.key))
        return self.key

    # 利用纠错编码生成最后的密钥
    def error_correction_slave(self):
        # 首先生成自己的纠错编码
        self.error_corr = encode(self.key)
        # 进行纠错编码的交换
        # slave首先将自己的发送出去
        # 密钥的纠错码不会超过190
        if len(self.error_corr) > 198:
            print("密钥长度超过198")
        self.uart_commu.send_data(self.error_corr)
        self.rece_error_corr = self.uart_commu.receive()
        print("纠错编码长度:", len(self.error_corr))
        print("接受到的纠错编码长度：", len(self.rece_error_corr))
        self.final_key = decode(self.key, self.rece_error_corr)
        print(len(self.final_key))
        print(self.final_key)
        self.uart_commu.send_end()
        self.get_byte_key()
        print(len(self.byte_key))
        print(self.byte_key)


    def erroe_correction_master(self):
        self.error_corr = encode(self.key)
        # 首先接受纠错编码
        self.rece_error_corr = self.uart_commu.receive()
        # 发送纠错编码
        if len(self.error_corr) > 198:
            print("纠错编码长度超过198")
        self.uart_commu.send_data(self.error_corr)
        print("纠错编码长度:", len(self.error_corr))
        print("接受到的纠错编码长度：", len(self.rece_error_corr))
        self.final_key = decode(self.key, self.rece_error_corr)
        print(len(self.final_key))
        print(self.final_key)
        self.get_byte_key()
        print(len(self.byte_key))
        print(self.byte_key)


    def get_key_master(self):
        while len(self.rssi_data) > 10:
            # print("当前密钥长度:", len(self.key))
            # print("剩余数据长度", len(self.rssi_data))
            # print("总和长度：", len(self.key) + len(self.rssi_data))
            # 首先进行平滑
            smooth_data = deal.smooth(self.rssi_data, constValue.smooth_order)

            # 然后进行rank
            rank_data = deal.Rank(smooth_data, constValue.rank_order)

            # 进行双门限量化
            data_doubleq, delete_index = deal.doubleq(rank_data, constValue.doubleq_Fac)
            # print("此次发送的删除index长度:", len(delete_index))
            # print(delete_index)
            # # 先等待接受shuju
            # print("准备接受数据")
            delete_index_reve = self.uart_commu.receive()
            # print("接收到数据")
            # print("准备发送数据")
            # 此处考虑如果delete_inde的长度为0
            if (len(delete_index) == 0):
                self.uart_commu.send_data([255])
            else:
                self.uart_commu.send_data(delete_index)


            if len(delete_index_reve) == 1 and delete_index_reve[0] == 255:
                delete_index_reve = []
            # print("此次接受的删除index长度:", len(delete_index_reve))
            # print(delete_index_reve)

            tmp_key, tmp_delete = deal.codeGen(data_doubleq, delete_index, delete_index_reve)
            self.key.extend(tmp_key)

            self.rssi_data = deal.get_new_rssi(self.rssi_data, tmp_delete)
        print("密钥长度:", len(self.key))
        return self.key

    # 发送数据
    def send_data(self, data):
        self.uart_commu.send_data(data)
        if self.uart_commu.get_ack():
            print("发送成功")
        else:
            print("发送失败")
    # 接收数据
    def get_data(self):
        return self.uart_commu.receive()

    # 将八个byte转化成一个int
    def change_to_byte(self,data):
        print("此次进行转换的数据:")
        print(data)
        result = 0
        for i in range(len(data)):
            result += data[i] * pow(2, i)
        print(result)
        return result

    # 转化成byte的形式
    def get_byte_key(self):
        self.byte_key = []
        print("最后生成秘钥的长度")
        print(int(len(self.final_key) / 8))
        for i in range(int(len(self.final_key) / 8)):
            tmp_int = self.change_to_byte(self.final_key[i * 8:(i + 1) * 8])
            self.byte_key.append(tmp_int)

    # 加密
