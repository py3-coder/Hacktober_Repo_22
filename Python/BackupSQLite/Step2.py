import sqlite3
import io
from sqlite3 import Error


def sql_connection():
	try:
		conn = sqlite3.connect('Originaldatabase.db')
		return conn
	except Error:
		print(Error)


def sql_table(conn):
	
	cursor_object = conn.cursor()
	cursor_object.execute(
		"CREATE TABLE student(roll_no integer PRIMARY KEY,first_name text,\
		last_name text, class text, stream text,address text)")
	conn.commit()


conn = sql_connection()
sql_table(conn)
