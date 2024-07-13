# bakery.py

from .inventory import Inventory
import psycopg2
import os

class Bakery(Inventory):
    def __init__(self, item_name, stock, pastry_type):
        super().__init__(item_name, stock)
        self.pastry_type = pastry_type
        
        
            
    def add_to_db(self):
            conn = Bakery.connect_db()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO bakery (item_name, stock, pastry_type) VALUES (%s, %s, %s)",
                (self.item_name, self.stock, self.pastry_type)
            )
            conn.commit()
            cur.close()
            conn.close()

    @staticmethod
    def update_stock(item_name, new_stock):
            conn = Bakery.connect_db()
            cur = conn.cursor()
            cur.execute(
                "UPDATE bakery SET stock = %s WHERE item_name = %s",
                (new_stock, item_name)
            )
            conn.commit()
            cur.close()
            conn.close()

    @staticmethod
    def delete_item(item_name):
            conn = Bakery.connect_db()
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM bakery WHERE item_name = %s",
                (item_name,)
            )
            conn.commit()
            cur.close()
            conn.close()

    @staticmethod
    def get_all_items():
            conn = Bakery.connect_db()
            cur = conn.cursor()
            cur.execute("SELECT item_name, stock, pastry_type FROM bakery")
            rows = cur.fetchall()
            items = [Bakery(*row) for row in rows]
            cur.close()
            conn.close()
            return items