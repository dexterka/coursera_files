import os
from os import path

# Find out the sender's email address with the maximum occurrence in the file
file_name = input('Enter the name of the file: ')
file_path = path.abspath(path.join('..', '..', 'sample_files', file_name))
file_read = open(file_path, 'r')

counts = dict()

# Loop through the email addresses only
for line in file_read:
    if line.startswith('From '):
        words = line.split()
        email_address = words[1]
        counts[email_address] = counts.get(email_address, 0) + 1

max_count = None
word_max_count = None

# Find out the sender's email address with the highest occurrence
for word, count in counts.items():
    if max_count is None or count > max_count:
        max_count = count
        word_max_count = word

print(word_max_count, max_count)