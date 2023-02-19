from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from _product import Ui_MainWindow
from db import Db
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()   

        self.rowIndex = 0
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)    
        self.db = Db()
        self.ui.btnSaveCategory.clicked.connect(self.addCategory)
        self.loadDb()

    def loadDb(self):
        self.loadCategories()
        self.loadProducts()

    def loadCategories(self):
        categories = []
        for i in self.db.loadCategories():
            categories.append(i[0])
        self.ui.cBoxCategory.addItems(categories)

    def addCategory(self):
        # print(type(self.ui.leAddCategory.text()))
        name = self.ui.leAddCategory.text()
        self.db.addCategory(name)

    def loadProducts(self):
        products = []
        for i in self.db.loadProducts():
            products.append({'id':i[0],'brand':i[1],'model':i[2],'price':i[3],'category':i[4]})
        
        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(5)
        self.ui.tableProducts.setHorizontalHeaderLabels(('id','brand','model','price','category'))
        self.ui.tableProducts.setColumnWidth(0,10)
        self.ui.tableProducts.setColumnWidth(1,50)
        self.ui.tableProducts.setColumnWidth(2,50)
        self.ui.tableProducts.setColumnWidth(3,50)
        self.ui.tableProducts.setColumnWidth(4,50)

        for product in products:
            self.addTable(product)

    def addTable(self,product):
        self.ui.tableProducts.setItem(self.rowIndex,0, QTableWidgetItem(str(product['id'])))
        self.ui.tableProducts.setItem(self.rowIndex,1, QTableWidgetItem(product['brand']))
        self.ui.tableProducts.setItem(self.rowIndex,2, QTableWidgetItem(product['model']))
        self.ui.tableProducts.setItem(self.rowIndex,3, QTableWidgetItem(str(product['price'])))
        self.ui.tableProducts.setItem(self.rowIndex,4, QTableWidgetItem(product['category']))
        self.rowIndex+=1


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


app()