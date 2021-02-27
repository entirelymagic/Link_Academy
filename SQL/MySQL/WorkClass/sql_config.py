import mysql.connector
from mysql.connector import errors


class MySQLConnector:
    def __init__(self):
        self.con = self.__connect_to_db()
        self.cursor = self.con.cursor(dictionary=True)

    def __connect_to_db(self):
        """Connect"""
        return mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                passwd="root",
                auth_plugin='mysql_native_password',
        )

    def execute_sql_file(self, file):
        """Execute the sql file provided as a parameter
        The file can contain multiple SQL statement set by multi=True on cursor.execute()
        """

        with open(file, "r") as f:
            data = f.read()
            try:
                self.cursor.execute(data, multi=True)
                self.con.commit()

            except mysql.connector.Error as err:
                print(err)
                print("Error Code:", err.errno)
                print("SQLSTATE", err.sqlstate)
                print("Message", err.msg)

    def print_cursor_items(self):
        """Iterate over the cursor and print the items presents"""
        for item in self.cursor:
            print(item)
