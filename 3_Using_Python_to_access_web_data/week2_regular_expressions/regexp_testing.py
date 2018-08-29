import re  # regular expression library
from os import path

file_name = input('Enter the name of the file: ')
file_path = path.abspath(path.join('..', '..', 'sample_files', file_name))
file_read = open(file_path, 'r')

for line in file_read:
    line = line.rstrip()
    if re.search('From:', line):  # finds the text with the search pattern (like string.find())
        print('1:', line)
    if re.search('^From:', line):
        print('2:', line)
    if re.search('^X.*:', line):  # starts with X followed by one or more characters and a colon
        print('3:', line)
    if re.search('^X-\S+:', line):  # starts with X followed by dash, one or more non-white spaces and a colon
        print('4:', line)
    numbers = re.findall('[0-9]+', line)  # extracts numbers with one or more digits
    print('5:', line, numbers)  # returns a list of string values
    uppercase = re.findall('[AEIOU]+', line)  # extracts one or more upper-case letters
    print('6:', line, uppercase)
    not_greedy = re.findall('^B.+?', line)  # starts with B followed by one or more characters but not in a greedy way
    print('7:', line, not_greedy)
    email_address = re.findall('\S+@\S+', line)  # find at-sign surrounded by one or more non-blank characters
    print('Email:', line, email_address)
    email_address2 = re.findall('^From (\S+@\S+)', line)
    print('Email address 2:', line, email_address2)
    domain = re.findall('@([^ ]+)', line)  # find one or more non-blank characters after at-sign
    print('Domain:', line, domain)

text = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
reg = re.findall('\S+?@\S+', text)
print(reg)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)