# Env setup
import sqlite3
import xml.etree.ElementTree as ET
from os import path

# Db connection and path to the database
connect = sqlite3.connect(path.abspath(path.join('..', '..', 'sample_files', 'db', 'week3_tracks.sqlite')))
cursor = connect.cursor()

# Create the db structure
# executes multiple SQL commands delimited by semicolon
cursor.executescript('''
    DROP TABLE IF EXISTS Artist; 
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track
    ''')
cursor.executescript('''
    CREATE TABLE Artist
     (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      name TEXT UNIQUE);
    CREATE TABLE Album
     (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
      artist_id  INTEGER,
      title TEXT UNIQUE);
    CREATE TABLE Track 
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
     title TEXT UNIQUE,
     album_id INTEGER,
     length INTEGER,
     rating INTEGER,
     count INTEGER)
     ''')

# User's input
file_name = input('Enter the name of the XML file: ')

# if len(file_name) < 1:
#     file_name = 'Library.xml'

file_path = path.abspath(path.join('..', '..', 'sample_files', file_name))
file_read = open(file_path)

# Parse XML
xml_tree = ET.parse(file_read)
xml_tags = xml_tree.findall('dict/dict/dict')
print('There are %d records in the XML file.' % len(xml_tags))

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
    count = lookup(item, 'Play Count')
    rating = lookup(item, 'Rating')
    length = lookup(item, 'Total Time')

    if name is None or artist is None or album is None:
        continue

    print('Name:', name, 'Artist:', artist, 'Album:', album, 'Play count:', count, 'Rating:', rating, 'Length:', length)

    # Load entries to db
    # artist
    cursor.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cursor.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    artist_id = cursor.fetchone()[0]
    # album
    cursor.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?,?)', (album, artist_id))
    cursor.execute('SELECT id FROM Album where title = ?', (album, ))
    album_id = cursor.fetchone()[0]
    # track
    cursor.execute('INSERT OR REPLACE INTO Track (title, album_id, length, rating, count) VALUES (?,?,?,?,?)', (name, album_id, length, rating, count))

# Commit entries to db
connect.commit()

# Close the db connection
cursor.close()
connect.close()