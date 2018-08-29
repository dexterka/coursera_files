# Env setup
import urllib.request
import json

# Temp vars
total = 0

# User's input
url_name = input('Enter location: ')
html_request = urllib.request.Request(url_name, headers={'User-Agent': 'Mozilla/5.0'})
html_read = urllib.request.urlopen(html_request).read()

# Parse JSON data
json_data = json.loads(html_read)
list_of_dict = json_data['comments']

for item in list_of_dict:
    extract = item['count']
    number = int(extract)
    total = total + number

# Print results
print('Retrieving', url_name)
print('Retrieved %d characters' % len(html_read))
print('Count:', len(list_of_dict))
print('Sum:', total)