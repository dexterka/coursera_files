# WHILE loop
n = 5
while n > 0:
    print(n)
    n = n - 1
print('End of WHILE loop:', n)


# FOR loop
for i in [5,4,3,2,1]:
    print(i)
print('End of FOR loop:', i)


friends = ['Joseph', 'Sally', 'Peter']
for friend in friends:
    print('Happy New Year', friend, '!')
print('All done!')


# Find the maximum value from a given list
max_number = None

for i in [9, 41, 12, 3, 74, 15]:
    if max_number is None:
        max_number = i
    elif i > max_number:
        max_number = i
    print('Number from list:', i, 'Largest number:', max_number)

print('The largest number is:', max_number)


# Count the number of loops
start = 0

for i in [9, 41, 12, 3, 74, 15]:
    start = start + 1
    print('Order of loops:', start, 'Number from list:', i)

print('The number of loops:', start)


# Sum the values within loop
start = 0

for i in [9, 41, 12, 3, 74, 15]:
    start = start + i
    print('Subtotals:', start, 'Number from list:', i)

print('The sum of values in a list:', start)


# Find the average within loop
count = 0
sum = 0

for i in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + i
    print('Count:', count, 'Sum:', sum, 'Number from list:', i)

print('The average value:', sum / count)


# Filtering in a loop
count = 0

for i in [9, 41, 12, 3, 74, 15]:
    if i > 20:
        count = count + 1
        print('This number is greater than 20:', i)

# print('There are', count, 'numbers greater than 20.')
print('There are %d numbers greater than 20.' % count)


# Searching in a loop using a boolean variable
start = False

for i in [9, 41, 12, 3, 74, 15]:
    if i == 3:
        start = True
    print('Number from list:', i, 'Has the number been found yet?', start)

print('All done!', start)


# Find the smallest value from a given list
min_number = None

for i in [9, 41, 12, 3, 74, 15]:
    if min_number is None:
        min_number = i
    elif i < min_number:
        min_number = i
    print('Number from list:', i, 'The smallest number is:', min_number)

print('The smallest number is:', min_number)




