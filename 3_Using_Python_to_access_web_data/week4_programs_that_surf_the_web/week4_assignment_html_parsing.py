# Env setup
import urllib.request
from bs4 import BeautifulSoup

# Temp vars
cnt = 0
total = 0

# Simulate browser's behaviour
html_request = urllib.request.Request('http://py4e-data.dr-chuck.net/comments_101041.html', headers={'User-Agent': 'Mozilla/5.0'})
# Read the content of the web page and parse it accordingly
html_read = urllib.request.urlopen(html_request).read()
html_parse = BeautifulSoup(html_read, 'html.parser')

# Look for the content within the span tag
span_tags = html_parse('span')

for span_tag in span_tags:
    # print('Tag:', span_tag)
    # print('URL:', span_tag.get('span', None))
    # print('Attributes:', span_tag.attrs)
    extract = span_tag.contents[0]
    number = int(extract)
    cnt = cnt + 1
    total = total + number

# Print the results
print('Count of numbers:', cnt)
print('Sum of numbers:', total)

