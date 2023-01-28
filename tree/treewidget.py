import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = Ui()
        ui.setup_ui(self,app)
        
class Ui():
    def __init__(self):
        super().__init__()
    
    def setup_ctr(self,MainWindow,app):
        self.app = app
        self.win = MainWindow
        self.win.setWindowTitle("Macro")
        self.win.setGeometry(100,100,500,300)
        self.ctr_wid = QWidget(self.win)
        self.ctr_lay = QVBoxLayout(self.ctr_wid)
        self.win.setCentralWidget(self.ctr_wid)
    
    def setup_ui(self,MainWindow,app):
        col_num = 5
        self.setup_ctr(MainWindow,app)
        self.tw = TreeWidget(self.ctr_wid)
        self.tw.setColumnCount(col_num)
        self.ctr_lay.addWidget(self.tw)
        
class TreeWidget(QTreeWidget):
    def __init__(self,parent):
        super().__init__()
        self.root = self.invisibleRootItem()
        
        self.item = QTreeWidgetItem()
        self.item.setText(0,"item")
        self.root.addChild(self.item)
        
        #self.insertTopLevelItem(0,self.item)
        #self.item.insertChild(1,self.item)
        
        self.child0 = QTreeWidgetItem()
        self.child0.setText(0,"child0")
        self.item.insertChild(0,self.child0)
        
        self.child1 = QTreeWidgetItem()
        self.child1.setText(0,"child1")
        self.item.insertChild(0,self.child1)
        
        #insertChildren
        self.child2 = QTreeWidgetItem()
        self.child2.setText(0,"child2")
        
        
        self.child3 = QTreeWidgetItem()
        self.child3.setText(0,"child3")
        
        self.children_list = [self.child2,self.child3]
        self.item.insertChildren(0,self.children_list)
        
        self.child4 = QTreeWidgetItem()
        self.child4.setText(0,"child4")
        self.child3.insertChild(0,self.child4)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    app.exec_()