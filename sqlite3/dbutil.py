import sqlite3
from flask import _app_ctx_stack, Flask


# Instantiate the Node
app = Flask(__name__)

DATABASE = "C:/sqlite/TutorialsSampleDB"
def get_conn():
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except Exception as e:
        print(e)

    return None



@app.teardown_appcontext
def close_connection(exception):
    top = _app_ctx_stack
    if hasattr(top, "sqlite_db"):
        top.sqlite_db.close()


def query_db(query, args=(), one=False):
    cur = get_conn().cursor()
    cur.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    for row in rows:
        print(row)
    return rows

def dml_db(query, args=()):
    conn= get_conn()
    try :
        cur = conn.cursor()
        cur.execute(query, args)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    query = 'select * from students where StudentName like ?'
    args=['J%']
    print (query_db(query, args, one=False))

