import os
from os import path

purse = dict()

# Defining key-value pairs
purse['grocery'] = 10
purse['health'] = 12
purse['sport'] = 5

purse['grocery'] = purse['grocery'] + 5
print(purse['grocery'])

print(type(purse))


# Counting the occurrences of names
names = ['Bob', 'Mary', 'Peter', 'Mary', 'Harry', 'Peter', 'Bob', 'Mary']
counts = dict()

# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
#     print(counts)

# shorter way
for name in names:
    counts[name] = counts.get(name, 0) + 1
    print(counts)


# Read the user's input and find the word with the highest occurrence
counts = dict()

text = input('Enter your text here: ')

text = text.rstrip()
words = text.split()
print('Words:', words)
print('Type:', type(words))

for word in words:
    counts[word] = counts.get(word, 0) + 1

print('Counts:', counts)


# Iterating through dictionaries
for key in purse:
    print('Keys and values within the dictionary:', key, purse[key])


# Printing the key, values and items of a dictionary
print('Keys:', purse.keys())
print('Values:', purse.values())
print('Items:', purse.items())  # returns tuples: a list of key-value pairs

for key, value in purse.items():  # Python can have more than one iteration variable
    print(key, value)


# Find the most frequently occurring word in a file
file_name = input('Enter the name of the file: ')
file_path = path.abspath(path.join('..', '..', 'sample_files', file_name))
file_read = open(file_path, 'r')

counts = dict()

for line in file_read:
    words = line.split()
    print(line)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        print(word)

print(counts)

max_count = None
word_max_count = None

for word, count in counts.items():
    if max_count is None or count > max_count:
        max_count = count
        word_max_count = word

print('Word with highest occurrence:', word_max_count)
print('Word', word_max_count, 'was found %d times in the text.' % max_count)