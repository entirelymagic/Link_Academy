import config
import os
import mysql.connector

# make connection to database
con = config.connect()
# open cursor
db_cursor = con.cursor(dictionary=True)


def execute_sql(file, multi=False):
    with open(file, "r") as f:
        data = f.read()

        try:
            db_cursor.execute(data, multi)
            con.commit()

        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)


file = r'comenzi\insert_into_profesori.sql'

execute_sql(file)
