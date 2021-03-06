import mysql.connector


def connect():
    return mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="root",
            auth_plugin='mysql_native_password',
            database="facultate",
            )