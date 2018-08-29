# Env setup
import sqlite3
import xml.etree.ElementTree as ET
from os import path

# Connect to db and path to the saved db
connect = sqlite3.connect(path.abspath(path.join('..', '..', 'sample_files', 'db', 'week3_assignment_library_xml.sqlite')))
cursor = connect.cursor()

# Create db structure
cursor.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track
''')

cursor.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
     );
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
    );
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
    );
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
    )
''')

# User's input
file_name = input('Enter the name of the XML file: ')
file_path = path.abspath(path.join('..', '..', 'sample_files', file_name))
file_read = open(file_path)

# Parse XMl file
xml_tree = ET.parse(file_read)
xml_tags = xml_tree.findall('dict/dict/dict')
print('There are %d records in the XMl file.' % len(xml_tags))

def lookup(value, key):
    found = False
    for child in value:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

for item in xml_tags:

    if (lookup(item, 'Track ID') is None):
        continue

    name = lookup(item, 'Name')
    artist = lookup(item, 'Artist')
    album = lookup(item, 'Album')
    genre = lookup(item, 'Genre')
    len = lookup(item, 'Total Time')
    rating = lookup(item, 'Rating')
    count = lookup(item, 'Play Count')

    if name is None or artist is None or album is None or genre is None:
        continue

    # Print the parsed results
    print('Name:', name, 'Artist:', artist, 'Album:', album, 'Genre:', genre, 'Total Time:', len, 'Rating:', rating, 'Play Count:', count)

    # Load items to db
    # artist
    cursor.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist, ))
    cursor.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    artist_id = cursor.fetchone()[0]
    # genre
    cursor.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre, ))
    cursor.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
    genre_id = cursor.fetchone()[0]
    # album
    cursor.execute('INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?,?)', (artist_id, album))
    cursor.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cursor.fetchone()[0]
    # track
    cursor.execute('INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?,?,?,?,?,?)', (name, album_id, genre_id, len, rating, count))

# Commit items into db
connect.commit()

# Close db connection
cursor.close()
connect.close()