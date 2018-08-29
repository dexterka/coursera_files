# Env setup
import urllib.request
from bs4 import BeautifulSoup

# Temp vars
lst_link_name = list()

# Read the provided web page and parse it
link = input('Enter the URL address: ')
count_input = int(input('Enter count: '))
position_input = int(input('Enter position: '))

# Repeat the loop n-th times based on input and look for a link at certain position
while count_input > 0:
    print('Retrieving URL address:', link)
    html_request = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    html_read = urllib.request.urlopen(html_request).read()
    html_parse = BeautifulSoup(html_read, 'html.parser')
    ahref_tags = html_parse('a')
    link = ahref_tags[position_input - 1]['href']
    link_name = ahref_tags[position_input - 1].contents
    lst_link_name.append(link_name)
    count_input = count_input - 1

# Print result
print('Name from last URL address:', lst_link_name[-1])