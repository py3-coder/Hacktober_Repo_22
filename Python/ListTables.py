# Importing Sqlite3 Module
import sqlite3

try:
	
	# Making a connection between sqlite3
	# database and Python Program
	sqliteConnection = sqlite3.connect('SQLite_Retrieving_data.db')
	
	# If sqlite3 makes a connection with python
	# program then it will print "Connected to SQLite"
	# Otherwise it will show errors
	print("Connected to SQLite")

	# Getting all tables from sqlite_master
	sql_query = """SELECT name FROM sqlite_master
	WHERE type='table';"""

	# Creating cursor object using connection object
	cursor = sqliteConnection.cursor()
	
	# executing our sql query
	cursor.execute(sql_query)
	print("List of tables\n")
	
	# printing all tables list
	print(cursor.fetchall())

except sqlite3.Error as error:
	print("Failed to execute the above query", error)
	
finally:

	# Inside Finally Block, If connection is
	# open, we need to close it
	if sqliteConnection:
		
		# using close() method, we will close
		# the connection
		sqliteConnection.close()
		
		# After closing connection object, we
		# will print "the sqlite connection is
		# closed"
		print("the sqlite connection is closed")
