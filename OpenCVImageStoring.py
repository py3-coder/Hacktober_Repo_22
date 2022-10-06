# import necessary libraries
import cv2
import sqlite3
import pandas as pd

# connect to database
conn = sqlite3.connect("gfg.db")
cursorObject = conn.cursor()

# create a table
cursorObject.execute("CREATE TABLE imgfg(id string, img blob)")
conn.commit()

# open the image you want to store in read more
im = open('gfg.png', 'rb').read()
conn.execute("INSERT INTO imgfg VALUES(?,?)",
			("pattern", sqlite3.Binary(im)))
conn.commit()

# Use pandas to create a dataframe from
# the table and save it as a csv
table = pd.read_sql_query("SELECT * FROM imgfg", conn)
table.to_csv("imgfg" + '.csv', index_label='index')

# display table
print(table)
