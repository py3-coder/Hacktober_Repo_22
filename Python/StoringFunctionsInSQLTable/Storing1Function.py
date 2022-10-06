# Importing required library
import sqlite3

# Initializing the database
conn = sqlite3.connect('function.db')

# Creating cursor object
c = conn.cursor()

# Creating table
c.execute('''CREATE TABLE pyfuction
			(func_defination TEXT)''')

# Storing a python function in the Sqlite table
def1 = """ def maximum(): print(max(2,5))"""
c.execute("INSERT INTO pyfuction (func_defination) VALUES (?)",
		(def1,))

# Storing another python function in the Sqlite table
def2 = """ def gfg(): print("GeeksforGeeks")"""
c.execute("INSERT INTO pyfuction (func_defination) VALUES (?)",
		(def2,))

# Displaying Content of the table
c.execute("SELECT * FROM pyfuction;")
print(c.fetchall())

# Terminating the transaction
conn.commit()
