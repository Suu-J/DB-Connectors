import snowflake.connector

# with tryexcept, just some quick add
USER = ""
PASSWORD = ""
ACCOUNT = ""
WAREHOUSE = ""
DATABASE = ""
SCHEMA = ""

try:
    
    conn = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        warehouse=WAREHOUSE,
        database=DATABASE,
        schema=SCHEMA
    )

    cur = conn.cursor()

    cur.execute("SELECT CURRENT_DATE()")

    result = cur.fetchone()[0]
    print("Current date in Snowflake:", result)

except snowflake.connector.errors.ProgrammingError as e:
    print("Snowflake Error:", e)

finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()
