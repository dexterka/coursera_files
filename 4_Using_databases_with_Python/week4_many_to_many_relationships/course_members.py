# Env setup
import json
import sqlite3
from os import path

# Create db connection and save the db
connect = sqlite3.connect(path.abspath(path.join('..', '..', 'sample_files', 'db', 'week4_course_members.sqlite')))
cursor = connect.cursor()

# Create db structure
cursor.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member
''')

cursor.executescript('''
CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
    );

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
    );
    
CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
    ) 
''')

# User's input
file_name = input('Enter the name of the file: ')
if len(file_name) < 1:
    file_name = 'roster_data.json'
file_path = path.abspath(path.join('..', '..', 'sample_files', file_name))
file_read = open(file_path).read()

# Parse JSON data
json_data = json.loads(file_read)

for item in json_data:
    user_name = item[0]
    course_title = item[1]
    user_role = item[2]
    print('User name:', user_name, 'Course title:', course_title, 'User role:', user_role)
    # Load entries to db tables
    # user
    cursor.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (user_name, ))
    cursor.execute('SELECT id FROM User WHERE name = ?', (user_name, ))
    user_id = cursor.fetchone()[0]
    # course
    cursor.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course_title, ))
    cursor.execute('SELECT id FROM Course WHERE title = ?', (course_title, ))
    course_id = cursor.fetchone()[0]
    # member
    cursor.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?,?,?)', (user_id, course_id, user_role))

# Commit entries to db
connect.commit()

# Close db connection
cursor.close()
connect.close()