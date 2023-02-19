from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from _product import Ui_MainWindow
from db import Db
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()   

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)    
        self.db = Db()
        self.loadDb()

    def loadDb(self):
        self.loadCategories()
        self.loadProducts()

    def loadCategories(self):
        categories = []
        for i in self.db.loadCategories():
            categories.append(i[0])
        self.ui.cBoxCategory.addItems(categories)

    def loadProducts(self):
        print(self.db.loadProducts())
        # products = []
        # for i in self.db.loadProducts():
        #     products.append({'id':i[0],'brand':i[1],'model':i[2],'price':i[3],'categoryId':i[4]})
        # print(products)

        # self.ui.tableProducts.setRowCount(len(products))
        # self.ui.tableProducts.setColumnCount(5)
        # self.ui.tableProducts.setHorizontalHeaderLabels(('id','brand','model','price','categoryId'))
        # self.ui.tableProducts.setColumnWidth(0,200)
        # self.ui.tableProducts.setColumnWidth(1,100)

        # rowIndex = 0
        # for product in products:
        #     self.ui.tableProducts.setItem(rowIndex,0, QTableWidgetItem(product['name']))
        #     self.ui.tableProducts.setItem(rowIndex,1, QTableWidgetItem(str(product['price'])))
            
        #     rowIndex+=1


        # self.ui.tableProducts.


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


app()