# Define list
friends = ['Bob', 'Harry', 'Anne', 'Peter', 'Helen', 'Mary']

print(friends[2:4])
print(type(friends))

friends[1] = 'Susan'
print(friends)

print('Length of list:', len(friends))


# A counted loop with range
for i in range(len(friends)):
    friend = friends[i]
    print('Index:', i)
    print('Happy New Year:', friend)


# Manipulating lists
lists = list()
print(lists)

lists.append(300)
lists.append('red')
lists.append(0.875)

print(lists)
print(type(lists))

friends.sort() # throws an error due to integers, string value and floating number = a mismatch
print(friends) # sorts alphabetically

numerals = [1,2,3,4,5,6]
print(sum(numerals))
print(max(numerals))
print(min(numerals))

text = 'I have some breaking news!'
splitted = text.split() # default is splitting by whitespaces
print(splitted)
print(len(splitted))

for word in splitted:
    print(word)

sentence = 'first;second;third'
splitted_delim = sentence.split(';')
print(splitted_delim)