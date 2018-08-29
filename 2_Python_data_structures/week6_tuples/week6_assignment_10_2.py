import os
from os import path

# Find out the hour distribution from the file
file_name = input('Enter the name of the file: ')
file_path = path.abspath(path.join('..', '..', 'sample_files', file_name))
file_read = open(file_path, 'r')

counts = dict()
lst = list()

# Retrieve the counts
for line in file_read:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hours = time.split(':')
        hour = hours[0]
        counts[hour] = counts.get(hour, 0) + 1

# Create tuples from dictionary and sort them by the hour
lst = sorted([(hour, count) for hour, count in counts.items()])

# Print the result
for hour, count in lst[:]:
    print(hour, count)