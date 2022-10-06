import sqlite3

# Connecting to sqlite
connection_obj = sqlite3.connect('geek.db')

# cursor object
cursor_obj = connection_obj.cursor()

# select from sqlite_master
cursor_obj.execute("SELECT * FROM sqlite_master")

table = cursor_obj.fetchall()
print("Before changing the name of Table")
print("The name of the table:", table[0][2])

# Rename the SQLite Table
renameTable = "ALTER TABLE GEEK RENAME TO GFG"
cursor_obj.execute(renameTable)


# select from sqlite_master
cursor_obj.execute("SELECT * FROM sqlite_master")

table = cursor_obj.fetchall()

print("After changing the name of Table")
print("The name of the table:", table[0][2])

connection_obj.commit()

connection_obj.close()
