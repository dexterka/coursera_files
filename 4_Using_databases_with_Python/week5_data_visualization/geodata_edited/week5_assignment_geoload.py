# Env setup
import json
import sqlite3
import urllib.request, urllib.parse
import time   # sleep time
from os import path

# Temp vars
count = 0

# Google Geocoding API setup
api_key = 'AIzaSyBagIqI1GsIInmH9RKkbDHFdSffV2fIiDw'

if api_key is False:
    serviceurl = 'http://python-data.dr-chuck.net/geojson?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Connect to db
connect = sqlite3.connect(path.abspath(path.join('..', '..', '..', 'sample_files', 'db', 'week5_assignment_geodata.sqlite')))
cursor = connect.cursor()

# Create db structure
cursor.executescript('''
    CREATE TABLE IF NOT EXISTS Location (
        address TEXT,
        gps_lat NUMBER,
        gps_lon NUMBER,
        formatted_address TEXT
        )
    ''')

# Read the data in where.data (my university appended to the end of the line)
file_path = path.abspath(path.join('..', '..', '..', 'sample_files', 'where.data'))
file_read = open(file_path)

for line in file_read:

    # Parse the where.data
    address = line.strip()

    # If the address is already in the database do not send it to the Google Geocoding API
    cursor.execute('SELECT address FROM Location WHERE address = ?', (address, ))
    try:
        cursor.fetchone()[0]
        print('Address:', address, 'was already found in the database.')
        continue
    except:
        pass

    # If the address is not in the database do send it to the Google Geocoding API
    print('Address:', address, 'is being sent to the Google Geocoding API.')
    url = serviceurl + urllib.parse.urlencode({'address': address}) + '&' + urllib.parse.urlencode({'key': api_key})
    url_read = urllib.request.urlopen(url)
    data = url_read.read().decode()
    print('Retrieving %d characters from Google Geocoding API.' % len(data))
    # Set the counter
    count = count + 1
    try:
        json_data = json.loads(data)
    except:
        json_data = None
    if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
        print('Failure to retrieve data from Google Geocoding API!!!')
        print(data)
        continue

    # Parse the JSON data
    gps_lat = json_data['results'][0]['geometry']['location']['lat']
    gps_lon = json_data['results'][0]['geometry']['location']['lng']
    formatted_address = json_data['results'][0]['formatted_address']

    # Load the retrieved geodata into the db
    cursor.execute('INSERT INTO Location (address, gps_lat, gps_lon, formatted_address) VALUES (?,?,?,?)', (address, gps_lat, gps_lon, formatted_address))

    # Commit the entries into the db
    connect.commit()

    # Sleep time
    if count % 100 == 0:
        print('A little pause here before the next batch of addresses are sent to the Google Geocoding API.')
        time.sleep(3)

# Close the db connection
connect.close()