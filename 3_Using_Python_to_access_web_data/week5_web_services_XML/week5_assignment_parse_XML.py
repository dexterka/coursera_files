# Env setup
import urllib.request
import xml.etree.ElementTree as ET

# Temp vars
total = 0

# User's input
url_name = input('Enter location: ')
html_request = urllib.request.Request(url_name, headers={'User-Agent': 'Mozilla/5.0'})
html_read = urllib.request.urlopen(html_request).read()

# Parse XML data
xml_tree = ET.fromstring(html_read)
list_of_tags = xml_tree.findall('comments/comment')

for tag in list_of_tags:
    extract = tag.find('count').text
    number = int(extract)
    total = total + number

# Print results
print('Retrieving:', url_name)
print('Retrieved %d characters' % len(html_read))
print('Count of comments:', len(list_of_tags))
print('Sum of numbers:', total)