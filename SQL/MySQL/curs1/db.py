import config


# make connection to database
con = config.connect()
# open cursor
db_cursor = con.cursor(dictionary=True)
# executing cursor with execute method and pass SQL query
# get list of all databases

# SQL = "CREATE SCHEMA `magazin` DEFAULT CHARACTER SET utf8 ;"
#
# db_cursor.execute(SQL)
#
# db_cursor.execute("SHOW DATABASES")
# # print all databases
# for db in db_cursor:
#     print(db)


def execute_sql(file):
    with open(file, "r") as f:
        data = f.read()
        db_cursor.execute(data)


file = 'comenzi/populate_produse_magazin.sql'

execute_sql(file)