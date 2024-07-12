# grocery.py

from .inventory import Inventory
import psycopg2
import os

class Grocery(Inventory):
    def __init__(self, item_name, stock, expiration_date):
        super().__init__(item_name, stock)
        self.expiration_date = expiration_date

    def add_to_db(self):
        conn = self.connect_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO grocery (item_name, stock, expiration_date) VALUES (%s, %s, %s)",
            (self.item_name, self.stock, self.expiration_date)
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_all_items():
        conn = Grocery.connect_db()
        cur = conn.cursor()
        cur.execute("SELECT item_name, stock, expiration_date FROM grocery")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [Grocery(*row) for row in rows]
    
    @staticmethod
    def update_stock(item_name, new_stock):
        conn = Grocery.connect_db()
        cur = conn.cursor()
        cur.execute(
            "UPDATE grocery SET stock = %s WHERE item_name = %s",
            (new_stock, item_name)
        )
        conn.commit()
        cur.close()
        conn.close()
        
    @staticmethod
    def delete_item(item_name):
        conn = Grocery.connect_db()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM grocery WHERE item_name = %s",
            (item_name,)
        )
        conn.commit()
        cur.close()
        conn.close()
