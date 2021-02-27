#import the module
import mysql.connector
def connect():
    return  mysql.connector.connect( 
            host="localhost",
            user="root",
            passwd="root",
            auth_plugin='mysql_native_password',
            )