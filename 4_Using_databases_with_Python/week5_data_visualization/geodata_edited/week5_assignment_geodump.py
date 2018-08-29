# Env setup
import sqlite3
import json
from os import path

# Create db connection
connect = sqlite3.connect(path.abspath(path.join('..', '..', '..', 'sample_files', 'db', 'week5_assignment_geodata.sqlite')))
cursor = connect.cursor()

# Retrieve all records from the db
cursor.execute('''
    SELECT 
        CAST(gps_lat as decimal),
        CAST(gps_lon as decimal),
        REPLACE(formatted_address, "'", "")
    FROM Location
    ''')
data_all = cursor.fetchall()

# Save the data to JSON file
with open('where.js', 'w', encoding='utf-8') as outfile:
    json.dump({'myData':data_all}, outfile, ensure_ascii=False)

# Count the number of rows from db
cursor.execute('SELECT COUNT(*) FROM Location')
count = cursor.fetchone()[0]

# Close the db connection
cursor.close()
connect.close()

# Print closing remarks
print('There are %d records written to where.js.' % count)
print('Please open where.html file in your browser to view the results.')