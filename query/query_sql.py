import psycopg2
import os
from dotenv import load_dotenv, find_dotenv
from sql import full_query

load_dotenv(find_dotenv())

def query_db():

    conn = psycopg2.connect(f"dbname= {os.environ.get('DBNAME')} \
                            user={os.environ.get('USER')} \
                            host={os.environ.get('HOST')} \
                            password={os.environ.get('PASSWORD')}")
    cur = conn.cursor()

    cur.execute(full_query)

    rows = cur.fetchall()

    return rows

if __name__ == '__main__':
    x = query_db()
    #x= os.environ
    print(x)
