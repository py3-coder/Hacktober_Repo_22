# importing sqlite3 module
import sqlite3


# create connection by using object
# to connect with hotel_data database
connection = sqlite3.connect('hotel_data.db')

# query to create a table named FOOD1
connection.execute(''' CREATE TABLE hotel
		(FIND INT PRIMARY KEY	 NOT NULL,
		FNAME		 TEXT NOT NULL,
		COST		 INT	 NOT NULL,
		WEIGHT	 INT);
		''')

# insert query to insert food details in
# the above table
connection.execute("INSERT INTO hotel VALUES (1, 'cakes',800,10 )")
connection.execute("INSERT INTO hotel VALUES (2, 'biscuits',100,20 )")
connection.execute("INSERT INTO hotel VALUES (3, 'chocos',1000,30 )")


print("All data in food table\n")

# create a cousor object for select query
cursor = connection.execute("SELECT * from hotel ")

# display all data from hotel table
for row in cursor:
	print(row)
