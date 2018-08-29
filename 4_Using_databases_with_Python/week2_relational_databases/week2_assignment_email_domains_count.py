# Env setup
import sqlite3
from os import path

# Db connection and path to created db
connect = sqlite3.connect(path.abspath(path.join('..', '..', 'sample_files', 'db', 'week2_assignment_email_domains_count.sqlite')))
cursor = connect.cursor()

# Delete the table if it exists
cursor.execute('DROP TABLE IF EXISTS Counts')

# Create the table
cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# User's input
file_name = input(' Enter the name of the file: ')
file_path = path.abspath(path.join('..', '..', 'sample_files', file_name))
file_read = open(file_path)

# Extract the domain from the email address and save it to the db
for line in file_read:
    if not line.startswith('From: '):
        continue
    line = line.split()
    extract = line[1]
    item = extract.split('@')
    org = item[1]
    cursor.execute('SELECT org, count FROM Counts WHERE org = ? ', (org,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute('INSERT INTO Counts(org, count) VALUES (?, 1)', (org,))
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))

connect.commit()

# Print results
query = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cursor.execute(query):
    print('Organization name:', str(row[0]), '; ' 'Count:', row[1])

# Close db connection
cursor.close()