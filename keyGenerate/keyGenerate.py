__author__ = 'cao'
from Uart.uart import uart_communicate
import keyGenerate.dealData as deal
from Tools.ConstValue import constValue

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

    def get_key_master(self):
        while len(self.rssi_data) > 10:
            print("当前密钥长度:", len(self.key))
            print("剩余数据长度", len(self.rssi_data))
            print("总和长度：", len(self.key ) + len(self.rssi_data))
            # 首先进行平滑
            smooth_data = deal.smooth(self.rssi_data, constValue.smooth_order)

            # 然后进行rank
            rank_data = deal.Rank(smooth_data, constValue.rank_order)

            # 进行双门限量化
            data_doubleq, delete_index = deal.doubleq(rank_data, constValue.doubleq_Fac)
            print("此次发送的删除index长度:", len(delete_index) )
            print("准备发送数据")
            # 此处考虑如果delete_inde的长度为0
            if (len(delete_index) == 0):
                self.uart_commu.send_data([101])
            else:
                self.uart_commu.send_data(delete_index)
            print(delete_index)
            delete_index_reve = self.uart_commu.receive()

            if len(delete_index_reve) == 1 and delete_index_reve[0] == 101:
                delete_index_reve = []
            print("此次接受的删除index长度:", len(delete_index_reve))
            print(delete_index_reve)

            tmp_key, tmp_delete = deal.codeGen(data_doubleq, delete_index, delete_index_reve)
            self.key.extend(tmp_key)

            self.rssi_data = deal.get_new_rssi(self.rssi_data, tmp_delete)

    def get_key_slave(self):
        while len(self.rssi_data) > 10:
            print("当前密钥长度:", len(self.key))
            print("剩余数据长度", len(self.rssi_data))
            print("总和长度：", len(self.key) + len(self.rssi_data))
            # 首先进行平滑
            smooth_data = deal.smooth(self.rssi_data, constValue.smooth_order)

            # 然后进行rank
            rank_data = deal.Rank(smooth_data, constValue.rank_order)

            # 进行双门限量化
            data_doubleq, delete_index = deal.doubleq(rank_data, constValue.doubleq_Fac)
            print("此次发送的删除index长度:", len(delete_index))
            print(delete_index)
            # 先等待接受shuju
            print("准备接受数据")
            delete_index_reve = self.uart_commu.receive()
            print("准备发送数据")
            # 此处考虑如果delete_inde的长度为0
            if (len(delete_index) == 0):
                self.uart_commu.send_data([101])
            else:
                self.uart_commu.send_data(delete_index)


            if len(delete_index_reve) == 1 and delete_index_reve[0] == 101:
                delete_index_reve = []
            print("此次接受的删除index长度:", len(delete_index_reve))
            print(delete_index_reve)

            tmp_key, tmp_delete = deal.codeGen(data_doubleq, delete_index, delete_index_reve)
            self.key.extend(tmp_key)

            self.rssi_data = deal.get_new_rssi(self.rssi_data, tmp_delete)