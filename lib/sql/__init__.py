import os

import psycopg2

# Extract host and port from ngrok address
host, port = os.environ.get('SQL_HOST'), os.environ.get('SQL_PORT')

# PostgreSQL connection parameters
dbname = os.environ.get('SQL_DB_NAME')
user = os.environ.get('SQL_USERNAME')
password = os.environ.get('SQL_PASSWORD')


def create_connection():
    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )


if __name__ == "__main__":
    conn = create_connection()
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT version();")

    # Fetch and print the result
    db_version = cur.fetchone()
    print("Connected to:", db_version)
