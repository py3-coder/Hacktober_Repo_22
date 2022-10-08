# importing sqlite3 module
import sqlite3

# create connection by using object
# to connect with gfg database
connection = sqlite3.connect('gfg.db')


# insert query to insert student details
# in the above table
connection.execute(
	"INSERT INTO STUDENTS VALUES (5, 'mohan pavan', 22, 'ponnur' )")

connection.execute(
	"INSERT INTO STUDENTS VALUES (6, 'sudheer', 28, 'chebrolu' )")

connection.execute(
"INSERT INTO STUDENTS VALUES (7, 'mohan', 22, 'tenali' )")

# creating cursor object to display all
# the data in the table
cursor = connection.execute("SELECT * from STUDENTS")

# display data
print('\nOriginal Table:')
for row in cursor:
	print(row)

# update query to update ADDRESS
connection.execute("UPDATE STUDENTS set ADDRESS = 'naga' where SAGE = 22")

# save the changes
connection.commit()

# creating cursor object to display
# all the data in the table
cursor = connection.execute("SELECT * from STUDENTS")

# display data
print('\nUpdated Table:')
for row in cursor:
	print(row)
