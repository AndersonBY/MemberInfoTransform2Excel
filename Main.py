# -*- coding: utf-8 -*-
'''
Created on 2014年9月16日

@author: Ying
'''

import sys
import os
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import Qt
from MainWindow_ui import Ui_MainWindow
import xlrd
import xlsxwriter
import json


class MyMainWindow(Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__()
        # QtGui.QMainWindow.__init__(self,parent)
        self.ui = Ui_MainWindow(self)
        self.ui.setupUi(self)
        self.setupConnect()

    def setupConnect(self):
        self.ui.pushButton_transform.clicked.connect(self.onTransform)

    def onTransform(self):
        tmpFilePath = QtGui.QFileDialog.getOpenFileName(self,
                                                                "Choose TXT file to open",
                                                                "",
                                                                "TXT File (*.txt)")
        f = open(tmpFilePath)
        fileName = os.path.basename(tmpFilePath)
        excelFile = xlsxwriter.Workbook(fileName + '.xlsx')
        table = excelFile.add_worksheet(fileName)
        table.write_string(0, 0, "姓名")
        table.write_string(0, 1, "性别")
        table.write_string(0, 2, "电子邮箱")
        table.write_string(0, 3, "学号")
        table.write_string(0, 4, "电话")
        table.write_string(0, 5, "班号")
        table.write_string(0, 6, "院系")
        line = f.readline()  # 调用文件的 readline()方法
        i = 1
        while line:
            print(line, end='')  # 在 Python 3中使用
            start_index = line.find('{')
            if not start_index == -1:
                end_index = line.find('}')
                info_str = line[start_index: end_index + 1]
                print(info_str)
                try:
                    js = json.loads(info_str)  # 加载Json文件
                    table.write_string(i, 0, js["姓名"])
                    table.write_string(i, 1, js["性别"])
                    table.write_string(i, 2, js["电子邮箱"])
                    table.write_string(i, 3, js["学号"])
                    table.write_string(i, 4, js["电话"])
                    table.write_string(i, 5, js["班号"])
                    table.write_string(i, 6, js["院系"])
                    i = i + 1
                except:
                    print('bad line')
                    continue
                print(js)
            line = f.readline()
        f.close()
        excelFile.close()
        QtGui.QMessageBox.information(self, "Done",
                    "Done",
                    QtGui.QMessageBox.Ok, QtGui.QMessageBox.NoButton,
                    QtGui.QMessageBox.NoButton)

app = QtGui.QApplication(sys.argv)
widget = MyMainWindow()
widget.show()
sys.exit(app.exec_())
