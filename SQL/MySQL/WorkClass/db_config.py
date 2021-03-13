from sql_config import MySQLConnector


db = MySQLConnector()

# Set destination of the file
# file = 'sql_commands/command.sql'

file = 'sql_commands/dql_execute.sql'

db.execute_sql_file(file)
data = db.cursor.fetchall()

print(data)

