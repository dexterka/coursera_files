# Env setup
import sqlite3
from os import path

# Db connection and path to saved database
conn = sqlite3.connect(path.abspath(path.join('..', '..', 'sample_files', 'db', 'week2_emails.sqlite')))
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (email VARCHAR2, count NUMBER)')

# User's input
file_name = input('Enter file name: ')
file_path = path.abspath(path.join('..', '..', 'sample_files', file_name))
if len(file_name) < 1:
    file_name = 'mbox-short.txt'
file_read = open(file_path)

# Extract the email addresses from the file and load them into a database
for line in file_read:
    if not line.startswith('From: '):
        continue
    extract = line.split()
    email = extract[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()  # write the results from the memory into the db

# https://www.sqlite.org/lang_select.html
query = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(query):
    print(str(row[0]), row[1])

# Close db connection
cur.close()