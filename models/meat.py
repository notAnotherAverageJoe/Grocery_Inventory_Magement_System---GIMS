# meat.py

from .inventory import Inventory
import psycopg2
import os

class Meat(Inventory):
    def __init__(self, item_name, stock, cut_type):
        super().__init__(item_name, stock)
        self.cut_type = cut_type

    def add_to_db(self):
        conn = Meat.connect_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO meat (item_name, stock, cut_type) VALUES (%s, %s, %s)",
            (self.item_name, self.stock, self.cut_type)
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def update_stock(item_name, new_stock):
        conn = Meat.connect_db()
        cur = conn.cursor()
        cur.execute(
            "UPDATE meat SET stock = %s WHERE item_name = %s",
            (new_stock, item_name)
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def delete_item(item_name):
        conn = Meat.connect_db()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM meat WHERE item_name = %s",
            (item_name,)
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_all_items():
        conn = Meat.connect_db()
        cur = conn.cursor()
        cur.execute("SELECT item_name, stock, cut_type FROM meat")
        rows = cur.fetchall()
        items = [Meat(*row) for row in rows]
        cur.close()
        conn.close()
        return items