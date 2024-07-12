# models.produce

from .inventory import Inventory
import psycopg2
import os

class Produce(Inventory):
    def __init__(self, item_name, stock, in_season):
        super().__init__(item_name, stock)
        self.in_season = in_season
        
        
    def add_to_db(self):
        conn = Produce.connect_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO produce (item_name, stock, in_season) VALUES (%s, %s, %s)",
            (self.item_name, self.stock, self.in_season)
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def update_stock(item_name, new_stock):
        conn = Produce.connect_db()
        cur = conn.cursor()
        cur.execute(
            "UPDATE produce SET stock = %s WHERE item_name = %s",
            (new_stock, item_name)
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def delete_item(item_name):
        conn = Produce.connect_db()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM produce WHERE item_name = %s",
            (item_name,)
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_all_items():
        conn = Produce.connect_db()
        cur = conn.cursor()
        cur.execute("SELECT item_name, stock, in_season FROM produce")
        rows = cur.fetchall()
        items = [Produce(*row) for row in rows]
        cur.close()
        conn.close()
        return items
    