# import module
import sqlite3

try:
	# establish connection
	sqliteConnection = sqlite3.connect('sqlite.db')
	
	# create cursor object
	cursor = sqliteConnection.cursor()
	print('Database Initialization and Connection successful')
	
	# display version
	query = 'select sqlite_version();'
	cursor.execute(query)
	
	# get data
	record = cursor.fetchall()
	print(f'SQLite Version - {record}')
	cursor.close()

except sqlite3.Error as error:
	print('Error occurred - ', error)
	
finally:
	# If the connection was established then close it
	if sqliteConnection:
		sqliteConnection.close()
		print('SQLite Connection closed')
