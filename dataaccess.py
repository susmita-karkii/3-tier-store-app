import sqlite3

class DataAccess:
    def __init__(self):
        self.conn = sqlite3.connect('three_layered_db.db')
        self.cur = self.conn.cursor()

    def insert_product(self, first_name, last_name, product_name):
        customer_id = self.get_customer_id(first_name, last_name)
        product_id = self.get_product_id(product_name)
        price = self.get_product_price(product_name)

        if not customer_id:
            customer_id = self.insert_customer(first_name, last_name)
            self.insert_basket(customer_id, price)
            basket_id = self.get_basket_id(customer_id)
            self.insert_basket_product(basket_id, product_id)
        else:
            self.insert_basket(customer_id, price)
            basket_id = self.get_basket_id(customer_id)
            self.insert_basket_product(basket_id, product_id)

    def get_purchases(self):
        query = """
            SELECT c.CustomerFirstName, c.CustomerLastName, p.ProductName, pp.ProductPrice
            FROM Customer AS c
            INNER JOIN Basket AS b ON c.CustomerId = b.CustomerId
            INNER JOIN Basket_Product AS bp ON b.BasketId = bp.BasketId
            INNER JOIN Product AS p ON p.ProductId = bp.ProductId
            INNER JOIN Product_Price AS pp ON pp.ProductId = p.ProductId;
        """
        self.cur.execute(query)
        purchases = self.cur.fetchall()
        return purchases

    def get_purchase_history(self, full_name):
        first_name, last_name = full_name.split()
        query = """
            SELECT p.ProductName, pp.ProductPrice
            FROM Customer AS c
            INNER JOIN Basket AS b ON c.CustomerId = b.CustomerId
            INNER JOIN Basket_Product AS bp ON b.BasketId = bp.BasketId
            INNER JOIN Product AS p ON p.ProductId = bp.ProductId
            INNER JOIN Product_Price AS pp ON pp.ProductId = p.ProductId
            WHERE c.CustomerFirstName = ? AND c.CustomerLastName = ?;
        """
        self.cur.execute(query, (first_name, last_name))
        history = self.cur.fetchall()
        return history

    def get_customer_id(self, first_name, last_name):
        query = """
            SELECT CustomerId
            FROM Customer
            WHERE CustomerFirstName = ? AND CustomerLastName = ?;
        """
        self.cur.execute(query, (first_name, last_name))
        customer = self.cur.fetchone()
        if customer:
            return customer[0]
        else:
            return None

    def get_product_id(self, product_name):
        query = """
            SELECT ProductId
            FROM Product
            WHERE ProductName = ?;
        """
        self.cur.execute(query, (product_name,))
        product = self.cur.fetchone()
        if product:
            return product[0]
        else:
            return None

    def get_product_price(self, product_name):
        query = """
            SELECT ProductPrice
            FROM Product_Price AS pp
            INNER JOIN Product AS p ON p.ProductId = pp.ProductId
            WHERE p.ProductName = ?;
        """
        self.cur.execute(query, (product_name,))
        price = self.cur.fetchone()
        if price:
            return price[0]
        else:
            return None

    def insert_customer(self, first_name, last_name):
        query = """
            INSERT INTO Customer (CustomerFirstName, CustomerLastName)
            VALUES (?, ?);
        """
        self.cur.execute(query, (first_name, last_name))
        self.conn.commit()
        return self.cur.lastrowid

    def insert_basket(self, customer_id, price):
        query = """
            INSERT INTO Basket (CustomerId, OrderDate, SumPrice)
            VALUES (?, date('now'), ?);
        """
        self.cur.execute(query, (customer_id, price))
        self.conn.commit()

    def insert_basket_product(self, basket_id, product_id):
        query = """
            INSERT INTO Basket_Product (BasketId, ProductId)
            VALUES (?, ?);
        """
        self.cur.execute(query, (basket_id, product_id))
        self.conn.commit()

    def get_basket_id(self, customer_id):
        query = """
            SELECT BasketId
            FROM Basket
            WHERE CustomerId = ?;
        """
        self.cur.execute(query, (customer_id,))
        basket = self.cur.fetchone()
        if basket:
            return basket[0]
        else:
            return None
