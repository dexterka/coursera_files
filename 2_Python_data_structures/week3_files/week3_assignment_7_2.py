import os
from os import path

# Read text file, search for pattern, compute average
file_name = input('Enter file name: ')
file_path = path.abspath(path.join('..', '..', 'sample_files', 'mbox-short.txt'))
file_read = open(file_path, 'r')

count = 0
together = 0

for line in file_read:
    if line.startswith('X-DSPAM-Confidence:'):
        line_clean = line.rstrip()
        start_pos = line_clean.find(':')
        result = line_clean[start_pos + 1: ]
        result_num = float(result)
        count = count + 1
        together = together + result_num

print('Average spam confidence:', together / count)