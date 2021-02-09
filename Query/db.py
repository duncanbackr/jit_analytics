import psycopg2
import config
from Query.sql import full_query


def latest_comments(okta_id, limit=5000):

    conn = psycopg2.connect(f"dbname= {config.DB_NAME} \
                            user={config.DB_USER)} \
                            host={config.DB_HOST)} \
                            password={config.DB_PASSWORD}")
    cur = conn.cursor()

    query_string = full_query(okta_id, limit)

    cur.execute(query_string)

    rows = cur.fetchall()

    return rows

#print(latest_comments(37, 100)[0:8])