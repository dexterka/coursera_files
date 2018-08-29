# Env setup
import urllib.request, urllib.parse
import json

while True:
    # User's input
    location = input('Enter location: ')
    if len(location) < 1:
        break

    # Construct URL to send to query the API
    base_url = 'http://py4e-data.dr-chuck.net/geojson?'
    url_request = base_url + urllib.parse.urlencode({'address': location})
    url_read = urllib.request.urlopen(url_request).read().decode()

    # Parse JSON data
    try:
        json_data = json.loads(url_read)
    except:
        json_data = None

    if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
        print('Fail to query the API with the given location!!!', url_request)
        print('The allowed list of locations is as follows:', url_read)
        continue

    # Print results
    print('Retrieving', url_request)
    print('Retrieved %d characters' % len(url_read))
    print('Place id', json_data['results'][0]['place_id'])
