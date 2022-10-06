import sqlite3
import io
from sqlite3 import Error


def SQLite_connection():
	
	try:	
		conn = sqlite3.connect('Originaldatabase.db')
		print("Connection is established successfully!")
		print("'originaldatabase.db' is created ")
		return conn
		
	except Error:
		print(Error)
		
	finally:
		conn.close()

SQLite_connection()
