import os
from os import path

# Read the TXT file line by line, split it into words and sort alphabetically
file_name = input('Enter the name of the file: ')
file_path = path.abspath(path.join('..', '..', 'sample_files', 'romeo.txt'))
file_read = open(file_path, 'r')
lst = list()

for line in file_read:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word not in lst:
            lst.append(word)
            lst.sort()

print(lst)