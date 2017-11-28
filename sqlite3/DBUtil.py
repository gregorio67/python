import sqlite3
from flask import _app_ctx_stack, Flask


# Instantiate the Node
app = Flask(__name__)

class DBUtil:
    def __init__(self, database):
       self.database = database
       self.conn = self.get_conn()

    def get_conn(self):
        try:
            conn = sqlite3.connect(self.database)
            return conn
        except Exception as e:
            print(e)

        return None

    def query_db(self, query, args=(), one=False):

        cur = self.conn.cursor()
        cur.execute(query, args)
        rows = cur.fetchall()
        cur.close()
        for row in rows:
            print(row)
        return rows

    def dml_db(self, query, args=()):

        try :
            cur = self.conn.cursor()
            cur.execute(query, args)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
           self.conn.close()
