import sqlite3

class Db:
    def __init__(self):
        self.connection = sqlite3.connect("products.db")
        self.cursor = self.connection.cursor()
        
    def loadCategories(self):
        self.cursor.execute("select name from category")
        return self.cursor.fetchall()

    def addCategory(self,name):
        sql = f"INSERT INTO category(name) VALUES ('{name}');" 
        self.cursor.execute(sql)
        self.connection.commit()

    def categoryId(self,category):
        sql = f"select id from category where name = '{category}'"
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    def productId(self,brand,model,price,categoryId):
        sql = f"select id from products where brand = '{brand}' and model = '{model}' and price = {price} and categoryID = {categoryId};"
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    def deleteById(self,id):
        sql = f"delete from products where id = {id};"
        self.cursor.execute(sql)
        self.connection.commit()

    def addProduct(self,brand,model,price,category):
        categoryId = self.categoryId(category)
        sql = f"INSERT INTO products(brand,model,price,categoryId) VALUES ('{brand}','{model}',{price},{categoryId});"
        self.cursor.execute(sql)
        self.connection.commit()
        return self.productId(brand,model,price,categoryId)


    def loadProducts(self):
        self.cursor.execute("select p.id, p.brand, p.model, p.price, c.name from products as p inner join category as c on p.categoryId = c.id")
        return self.cursor.fetchall()
        
    def closeDb(self):
        self.connection.close()
