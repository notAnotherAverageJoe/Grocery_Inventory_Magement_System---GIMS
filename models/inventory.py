# inventory.py

import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

class Inventory:
    def __init__(self, item_name, stock):
        self.item_name = item_name
        self.stock = stock

    @staticmethod
    def connect_db():
        return psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST")
        )

