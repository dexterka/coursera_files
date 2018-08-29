import os
from os import path

# Read file and convert the content to upper-case
file_name = input('Enter the name of the file: ')
file_path = path.abspath(path.join('..', '..', 'sample_files', 'words.txt'))
print(file_path)
file_read = open(file_path, 'r')

for line in file_read:
    line = line.rstrip()
    print(line.upper())
