__author__ = 'caocongcong'

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()
         # 实际界面绘制交给InitUi方法
        self.initUI()


    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(200, 200, 1000, 750)
        #设置窗口的标题
        self.setWindowTitle("密钥生成演示系统")
        #设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('../data/seu.png'))

        #显示窗口
        self.show()


if __name__ == '__main__':
    #创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())