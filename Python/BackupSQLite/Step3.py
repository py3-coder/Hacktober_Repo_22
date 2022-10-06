import sqlite3
import io
conn = sqlite3.connect('Originaldatabase.db')

# Open() function
with io.open('backupdatabase_dump.sql', 'w') as p:
		
	# iterdump() function
	for line in conn.iterdump():
		
		p.write('%s\n' % line)
	
print(' Backup performed successfully!')
print(' Data Saved as backupdatabase_dump.sql')

conn.close()
