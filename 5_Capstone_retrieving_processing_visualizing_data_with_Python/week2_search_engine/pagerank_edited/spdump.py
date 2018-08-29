import sqlite3
from os import path

conn = sqlite3.connect(path.abspath(path.join('..', '..', '..', 'sample_files', 'db', 'week2_assignment_spider.sqlite')))
cur = conn.cursor()

cur.execute('''SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url 
     FROM Pages JOIN Links ON Pages.id = Links.to_id
     WHERE html IS NOT NULL
     GROUP BY id ORDER BY inbound DESC''')

count = 0
for row in cur :
    if count < 50 : print(row)
    count = count + 1
print(count, 'rows.')
cur.close()
