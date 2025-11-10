# Checking Connections
import cx_Oracle

# details for conn
username = ""
password = ""
dsn = ""

try:
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    print("Connected to Oracle Database!")

    # Close the connection
    connection.close()
    print("Connection closed.")

except cx_Oracle.Error as error:
    print("Error connecting to Oracle Database:", error)