# Env setup
import re
from os import path

# Path to file
file_path = path.abspath(path.join('..', '..', 'sample_files', 'regex_sum_101039.txt'))
file_read = open(file_path, 'r')

cnt = 0
total = 0
lst = list()

# Loop through the text file, find all numbers and print the sum of them
for line in file_read:
    line = line.rstrip()
    extract = re.findall('[0-9]+', line)
    for value in extract:
        number = int(value)
        lst.append(number)
        cnt = cnt + 1
        total = total + number

print('List of all extracted numbers from a given file:', lst)
print('Count of numbers:', cnt)
print('Sum of numbers:', total)






