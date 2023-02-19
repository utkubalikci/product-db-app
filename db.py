import sqlite3

class Db:
    def __init__(self):
        self.connection = sqlite3.connect("products.db")
        self.cursor = self.connection.cursor()
        
    def loadCategories(self):
        self.cursor.execute("select name from category")
        return self.cursor.fetchall()

    def addCategory(self,name):
        self.cursor.execute("")

    def loadProducts(self):
        self.cursor.execute("select * from products")
        return self.cursor.fetchall()
        
    def closeDb(self):
        self.connection.close()
