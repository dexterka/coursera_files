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
connect = sqlite3.connect(path.abspath(path.join('..', '..', 'sample_files', 'db', 'week2_Twitter_friends_db.sqlite')))
cursor = connect.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS twitter_friends (name VARCHAR2, retrieved NUMBER, friends NUMBER)')

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
    cursor.execute('UPDATE twitter_friends SET retrieved = 1 WHERE name = ?', (twitter_account,)) # check it!
    if twitter_account == 'quit':
        break
    # if len(twitter_account) < 1:
    #     cursor.execute('SELECT name FROM twitter_friends WHERE retrieved = 0 LIMIT 1')
    #     try:
    #         twitter_account = cursor.fetchone()[0]
    #     except:
    #         print('No friends retrieved for the Twitter account given.')
    #         continue
    # Get a list of user's friends(=following)
    users = api.GetFriends(screen_name=twitter_account)  # total_count=5 limits the list of friends to 5
    # Populate the db table
    for u in users:
        cursor.execute('SELECT friends from twitter_friends WHERE name = ? LIMIT 1', (u.screen_name,))
        # print('List of friends:', [u.screen_name for u in users])
        try:
            count = cursor.fetchone()[0]
            cursor.execute('UPDATE twitter_friends SET friends = ? WHERE name = ?', (count + 1, u.screen_name))
            count_old = count_old + 1
        except:
            cursor.execute('INSERT INTO twitter_friends(name, retrieved, friends) VALUES(?, 0, 1)', (u.screen_name, ))
            count_new = count_new + 1
    print('Number of new accounts:', count_new, 'Number of already visited/retrieved:', count_old)

# Commit the updates and close the db connection
connect.commit()
cursor.close()