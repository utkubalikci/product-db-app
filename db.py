import sqlite3

class Db:
    def __init__(self):
        self.connection = sqlite3.connect("products.db")
        self.cursor = self.connection.cursor()
        
    def loadCategories(self):
        self.cursor.execute("select name from category")
        return self.cursor.fetchall()

    def addCategory(self,name):
        sql = "INSERT INTO category(name) VALUES (%s,)" 
        values = tuple(name)
        print(type(values))
        self.cursor.execute(sql,values)

    def loadProducts(self):
        self.cursor.execute("select p.id, p.brand, p.model, p.price, c.name from products as p inner join category as c on p.categoryId = c.id")
        return self.cursor.fetchall()
        
    def closeDb(self):
        self.connection.close()
