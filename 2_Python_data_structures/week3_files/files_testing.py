import os
from os import path

# Current working directory
cwd = os.getcwd()
print(cwd)

# Open a file, read data
# path must be constructed
base_path = path.dirname(__file__)
print(base_path)

file_path = path.abspath(path.join(base_path, '..', '2_Python_data_structures_notes.txt'))
print(file_path)

read_file = open(file_path, 'r') # just handles the opening of a file not the data itself!

data = read_file.read() # reads all data into one string
print(data[1:100])

# .read() method is better than looping through the file with for loop
# for i in data:
#     print(i)

# Count the number of lines
count = 0

for line in data:
    count = count + 1

print('The number of lines in the file is:', count)


# Find a certain line
for line in data:
    line = line.rstrip()
    if not line.startswith('+'):
        continue
    print(line)

# Newline
text = 'Hello\nWorld!'
print(text)


