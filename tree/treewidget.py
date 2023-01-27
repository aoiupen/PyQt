import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTreeWidget")
        self.setGeometry(100,100,1000,300)
        self.ctr_wid = QWidget(self)
        self.ctr_lay = QVBoxLayout(self.ctr_wid)
        self.setCentralWidget((self.ctr_wid))
        
        tw = QTreeWidget(self.ctr_wid)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    app.exec_()