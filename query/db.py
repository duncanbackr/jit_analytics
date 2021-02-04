import psycopg2
import os
from dotenv import load_dotenv, find_dotenv
from Query.sql import full_query

# TODO set this up so it looks for .env local and function envs in production
load_dotenv(find_dotenv())

def latest_comments(creator_id, limit=5000):

    conn = psycopg2.connect(f"dbname= {os.environ.get('DBNAME')} \
                            user={os.environ.get('DBUSER')} \
                            host={os.environ.get('HOST')} \
                            password={os.environ.get('PASSWORD')}")
    cur = conn.cursor()

    query_string = full_query(creator_id, limit)

    cur.execute(query_string)

    rows = cur.fetchall()

    return rows

#print(latest_comments(37, 100)[0:8])