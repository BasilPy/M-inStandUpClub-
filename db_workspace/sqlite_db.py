import sqlite3
import os
from datetime import datetime


class DataBaseCRUD:

    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(path, f'data/db_{datetime.today().strftime("%d_%m_%Y")}.db')
        self.db_conn = sqlite3.connect(f"{db_path}")
        self.curs = self.db_conn.cursor()

    def db_sqlite_for_today(self):
        try:
            self.db_conn.execute('''CREATE TABLE IF NOT EXISTS clients(
                id integer primary key AUTOINCREMENT,
                time TEXT,
                idTg integer,
                nikTg text,
                orders text,
                kaspi text
            );''')
            self.db_conn.commit()
            print("Clients Table created successfully")
        except sqlite3.Error as my_error:
            print("error: ", my_error)

    def insert_order_time_by_id(self, id_telega: int):
        pass

    def insert_client(self, time0: str, id_telega: int, nik_telega: str, orders: str, kaspi: str):
        time5 = "10"
        try:
            command = f"""INSERT INTO clients (time, idTg, nikTg, orders, kaspi)
            VALUES('{time0}', {id_telega}, '{nik_telega}', '{orders}', '{kaspi}')
            """
            self.curs.execute(command)
        except sqlite3.Error as my_error:
            print("error2: ", my_error)


db = DataBaseCRUD()
db.db_sqlite_for_today()
db.insert_client(datetime.today().strftime("%H:%M:%S"), 244623926, "Basil", "kolbasa", "Ok")
