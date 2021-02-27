from sql_config import MySQLConnector


db = MySQLConnector()

# Set destination of the file
# file = 'sql_commands/command.sql'

file = 'sql_commands/create_table_magazin_categorie.sql'

db.execute_sql_file(file)

print(db.cursor)

