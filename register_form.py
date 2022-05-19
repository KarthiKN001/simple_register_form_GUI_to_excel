# 2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
from reg import Ui_MainWindow
import datetime
import uuid
import csv


reg = pd.DataFrame(columns=['NAME', 'MOBILE.NO', 'EMAIL', 'INSTITUTION/COMPANY', 'TIMESTAMP', 'UUID'])


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("SIMPLE REGISTER FORM")
        self.data = []
        self.count = 0
        self.reg_button.pressed.connect(self.save_data)

    def save_data(self):
        self.count += 1
        self.data.append(self.name_input.text().upper())
        self.data.append(self.mobile_input.text())
        self.data.append(self.email_input.text())
        self.data.append(self.ic_input.text())
        ct = datetime.datetime.now()
        ts = ct.timestamp()
        self.data.append(ts)
        c = uuid.uuid1()
        self.data.append(c)
        global reg
        reg.loc[self.count] = [str(self.data[0]), self.data[1], str(self.data[2]), str(self.data[3]), float(self.data[4]),
                      self.data[5]]
        reg.to_csv('C:\\Users\\Desktop\\regis.csv', mode='w', header=True, index=False,
                   index_label=None)
        self.name_input.clear()
        self.mobile_input.clear()
        self.email_input.clear()
        self.ic_input.clear()
        self.data.clear()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
