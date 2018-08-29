# Retrieve the ASCII number for a letter and vice-versa
print(ord('H'))
print(chr(42))

# Connect and parse data from web page
import urllib.error, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import ssl

web_page = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()

for line in web_page:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)

# Simulate browser behaviour
req = urllib.request.Request('https://www.dr-chuck.com/page1.htm', headers={'User-Agent': 'Mozilla/5.0'})
web_page = urllib.request.urlopen(req)

for line in web_page:
    print(line.decode().strip())


# Use BeautifulSoup to retrieve specific html elements
# Ignore SSL certificate errors for https sites with certificates that are not in Python list
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_name = input('Enter url name: ')
html_request = urllib.request.Request(url_name, headers={'User-Agent': 'Mozilla/5.0'})
html_read = urllib.request.urlopen(html_request, context=ctx).read()
html_parser = BeautifulSoup(html_read, 'html.parser')

tags = html_parser('a')
print(tags)
for tag in tags:
    result = tag.get('href', None)
    print(result)


# HTTPS site without context works fine as well
url_name = input('Enter url name: ')
html_request = urllib.request.Request(url_name, headers={'User-Agent': 'Mozilla/5.0'})
html_read = urllib.request.urlopen(html_request).read()
html_parser = BeautifulSoup(html_read, 'html.parser')

tags = html_parser('a')
for tag in tags:
    print(tag.get('href', None))