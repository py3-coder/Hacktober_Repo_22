import sqlite3
from PIL import Image

# Function for Convert Binary
# Data to Human Readable Format
def convert_data(data, file_name):
	
	# Convert binary format to
	# images or files data
	with open(file_name, 'wb') as file:
		file.write(data)
	img = Image.open(file_name)
	print(img)

try:
	
	# Using connect method for establishing
	# a connection
	con = sqlite3.connect('SQLite_Retrieving_data.db')
	cursor = con.cursor()
	print("Connected Successfully")

	# Search from table query
	query = "SELECT * FROM Student"

	# using cursor object executing our query
	cursor.execute(query)
	
	# fectching all records from cursor object
	records = cursor.fetchall()
	
	# using for loop retrieving one by one
	# rows or data
	for row in records:
		
		# storing row[0] in name variable
		name = row[0]
		
		# printing name variable
		print("Student Name = ", name)
		
		# storing image (currently in binary format)
		image = row[1]
		
		# calling above convert_data() for converting
		# binary data to human readable
		convert_data(image, "D:\Internship Tasks\GFG\sqlite\\" + name + ".png")
		print("Yeah!! We have successfully retrieved values from database")

	# If we don't have any records in our database,
	# then print this
	if len(records) == 0:
		print("Sorry! Please Insert some data before reading from the database.")

# print exception if found any during program
# is running
except sqlite3.Error as error:
	print(format(error))

# using finally, closing the connection
# (con) object
finally:
	if con:
		con.close()
		print("SQLite connection is closed")
