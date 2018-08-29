# Env setup
import os
import twitter  # python-twitter library for handling the Twitter API, https://python-twitter.readthedocs.io/en/latest/
from dotenv import load_dotenv  # python-dotenv library for loading environmental variables from file
from pathlib import Path

# Load env vars
env_path = Path('../..') / '.env'
load_dotenv(dotenv_path=env_path)
# print(os.getenv("CONSUMER_KEY"))

# Initialize API
api = twitter.Api(
    consumer_key=os.getenv('CONSUMER_KEY'),
    consumer_secret=os.getenv('CONSUMER_SECRET'),
    access_token_key=os.getenv('TOKEN_KEY'),
    access_token_secret=os.getenv('TOKEN_SECRET')
)

# Verify credentials
# print(api.VerifyCredentials())

# Get user's status messages
statuses = api.GetUserTimeline(screen_name='havran', count=2)
print('Status messages:', [s.text for s in statuses])

# Get a list of user's friends
users = api.GetFriends()
print('List of friends:', [u.name for u in users])

print('API limit:', api.rate_limit.get_limit('friends/list'))
