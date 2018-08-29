# Env setup
import urllib.request, urllib.parse, urllib.error
import json

# Construct the address to query the Google Geocoding API
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
api_key = ''

# Encode the address and retrieve the decoded results
while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address': address}) + '&' + urllib.parse.urlencode({'key': api_key})
    url_read = urllib.request.urlopen(url)
    data = url_read.read().decode()

    try:
        json_data = json.loads(data)
    except:
        json_data = None

    if not json_data or 'status' not in json_data or json_data['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # Print all of the retrieved data in JSON structure
    # print(json.dumps(json_data, indent=4))  # opposite of json.loads()

    lat = json_data["results"][0]["geometry"]["location"]["lat"]
    lng = json_data["results"][0]["geometry"]["location"]["lng"]
    location = json_data['results'][0]['formatted_address']

    # Print the results
    print('Retrieving', url)
    print('Retrieved %d characters.' % len(data))
    print('Formatted address:', location)
    print('Latitude:', lat)
    print('Longitude:', lng)