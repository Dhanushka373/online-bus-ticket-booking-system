import mysql.connector

def connect_to_mysql():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ticket',
        port = '3306'
    )
    if connection.is_connected():
        print("Connected")
        return connection
    else:
        print("Not Connected")




