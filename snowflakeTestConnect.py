import snowflake.connector

# emptied the connection params, but warehouse is mandatory to mention even if you have a default one for your account
conn_params = {
    "account": "",
    "user": "",
    "password": "",
    "warehouse": "",
    "database": "",
    "schema": "",
}

conn = snowflake.connector.connect(**conn_params)

# cur for cursor
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM CONTENTWORKSPACE")

row_count = cur.fetchone()[0]
print("Row count:", row_count)

cur.close()
conn.close()