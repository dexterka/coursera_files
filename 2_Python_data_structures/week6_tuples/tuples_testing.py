import os
from os import path


names = ('Bob', 'Mary', 'Helen', 'Peter')
print(names[2])
print(type(names))

(a,b) = ('red', 10)
print(b)

shopping = {'grocery': 10, 'sports': 5, 'pharmacy': 8}
print(shopping)
print(type(shopping))

# Sort the dictionary by using the list of tuples
# By KEY of the dictionary
dict_items = shopping.items()
print(dict_items)

dict_sorted = sorted(dict_items)
print(dict_sorted)

# By VALUES of the dictionary
tmp = list()

for key, value in shopping.items():
    tmp.append((value, key))  # reverse order

print(tmp)

tmp = sorted(tmp, reverse=False)  # False for ascending order, True for descending order
print(tmp)


# Print out the top 10 most common words from a file
file_name = input('Enter the name of the file: ')
file_path = path.abspath(path.join('..', '..', 'sample_files', file_name))
file_read = open(file_path, 'r')

counts = dict()
lst = list()

# Words counter
for line in file_read:
    words = line.split()
    print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Reverse the order of key/values
# for word, count in counts.items():
#     lst.append((count, word))
#
# print('Reverse value and key:', lst)
# lst = sorted(lst, reverse=True)
# print('Sorted dictionary based on the values:', lst)

# Shorter way - list comprehension
lst = sorted([(count, word) for word, count in counts.items()], reverse=True)
print(lst)

# Print out the top 10 most common words from a file

print('Top 10 most common words:')

for count, word in lst[0:10]:
    print('Word:', word, ';', 'Count:', count)