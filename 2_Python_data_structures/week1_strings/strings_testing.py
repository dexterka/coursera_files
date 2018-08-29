# Strings and their index
fruit = 'pineapple'
print(fruit[1:6]) # pronounced as fruit sub 1 through to 6, 6 is not included: 1-2-3-4-5
print('Length of input:', len(fruit))

# Loop through strings
# WHILE loop
fruit = 'apple'
index = 0

while index < len(fruit):
    x = fruit[index]
    print('Index:', index, 'Letter:', x)
    index = index + 1

print('All done!')


# FOR loop
fruit = 'strawberry'

for i in fruit:
    print('Letter:', i)


# Count the number of 'a's in the word
fruit = 'banana'
count = 0

for i in fruit:
    if i == 'a':
        # print(i)
        count = count + 1

print('There are %d "a" characters in the given word:' % count, fruit)

if 'a' in fruit:
    print('A is in the word:', fruit)


# Concatenate
a = 'Hello'
b = 'world'

print(a + ' ' + b + '!')


# String library
greeting = '    Hello Bob!  '
print(greeting)

dir(greeting) # all the methods for string manipulation, str class
print(greeting.lower()) # object method
print(greeting.upper())
greeting.capitalize()

greeting.find('o')
greeting.find('z') # -1 if the character is not found

greeting.replace('Bob', 'Jane')
greeting.replace('o', 'y') # replaces all occurrences

greeting.lstrip() # left
greeting.rstrip() # right
greeting.strip()  # strips all whitespaces both from left and right

greeting.startswith('Bob')
greeting.startswith(' ') # starts with whitespace

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

