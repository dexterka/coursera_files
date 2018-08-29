# Env setup
import sqlite3
import twitter
import os
from dotenv import load_dotenv
from pathlib import Path
from os import path

# Temp vars
count_old = 0
count_new = 0

# Load env variables
env_path = Path('../..') / '.env'
load_dotenv(dotenv_path=env_path)

# Connect to db
connect = sqlite3.connect(path.abspath(path.join('..', '..', 'sample_files', 'db', 'week4_Twitter_friends_db.sqlite')))
cursor = connect.cursor()

# Create db structure
cursor.executescript('''
CREATE TABLE IF NOT EXISTS People (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    retrieved INTEGER
    );

CREATE TABLE IF NOT EXISTS Follows (
    from_id INTEGER,
    to_id INTEGER,
    UNIQUE(from_id, to_id)
)
''')

# Initialize Twitter API
api = twitter.Api(
    consumer_key=os.getenv('CONSUMER_KEY'),
    consumer_secret=os.getenv('CONSUMER_SECRET'),
    access_token_key=os.getenv('TOKEN_KEY'),
    access_token_secret=os.getenv('TOKEN_SECRET')
)

# Get the Twitter username friends and load them into a database table
while True:
    # User's input
    twitter_account = input('Enter the Twitter account name or "quit" to quit the prompt: ')
    if twitter_account == 'quit':
        break
    if len(twitter_account) < 1:
        cursor.execute('SELECT id, name FROM People WHERE retrieved = 0 LIMIT 1')
        try:
            (id, twitter_account) = cursor.fetchone()
        except:
            print('No unretrieved Twitter accounts found.')
            continue
    else:
        cursor.execute('SELECT id from People WHERE name = ? LIMIT 1', (twitter_account, ))
        try:
            id = cursor.fetchone()[0]
        except:
            cursor.execute('INSERT OR IGNORE INTO People (name, retrieved) VALUES (?, 0)', (twitter_account, ))
            connect.commit()
            if cursor.rowcount != 1:
                print('Error inserting Twitter account:', twitter_account)
                continue
            id = cursor.lastrowid
    # Get a list of user's friends(=following)
    users = api.GetFriends(screen_name=twitter_account)  # total_count=5 limits the list of friends to 5
    cursor.execute('UPDATE People SET retrieved = 1 where name = ?', (twitter_account, ))
    # Populate the db table
    for u in users:
        cursor.execute('SELECT id from People WHERE name = ? LIMIT 1', (u.screen_name,))
        print('List of friends:', [u.screen_name for u in users])
        try:
            friend_id = cursor.fetchone()[0]
            count_old = count_old + 1
        except:
            cursor.execute('INSERT OR IGNORE INTO People(name, retrieved) VALUES(?, 0)', (u.screen_name, ))
            connect.commit()
            if cursor.rowcount != 1:
                print('Error inserting Twitter account:', u.screen_name)
                continue
            friend_id = cursor.lastrowid
            count_new = count_new + 1
        cursor.execute('INSERT OR IGNORE INTO Follows (from_id, to_id) VALUES (?,?)', (id, friend_id))
    print('Number of new accounts:', count_new, 'Number of already visited/retrieved:', count_old)

# Commit the updates and close the db connection
connect.commit()
cursor.close()