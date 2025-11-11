import snowflake.connector

# Set the connection parameters
conn_params = {
    "account": "",
    "user": "",
    "password": "",
    "warehouse": "",
    "database": "",
    "schema": "",
}

# Connect to Snowflake
conn = snowflake.connector.connect(**conn_params)

# Create a cursor
cur = conn.cursor()

# Execute a query to get the row count from the table
cur.execute("SELECT COUNT(*) FROM CONTENTWORKSPACE")

# Fetch the row count
row_count = cur.fetchone()[0]
print("Row count:", row_count)

# Close the cursor and the connection
cur.close()
conn.close()