import numpy as np

# Print out the title and lastname of the person
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

print(list(map(split_title_and_name, people)))

# Convert the function into a lambda (anonymous function)


def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))

# Convert the function to list comprehension:
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

# print(times_tables())

lst = [j*i for i in range(10) for j in range(10)]
print(lst)

# Make a list of all possible user ids (2 letters + 2 digits, e.g. aa42)
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

for a in lowercase:
    for b in lowercase:
        for c in digits:
            for d in digits:
                print(a+b+c+d)

correct_answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]

print(correct_answer[:50]) # Display first 50 ids

# Testing arrays
old = np.array([[1, 1, 1],
                [1, 1, 1]])

new = old
new[0, :2] = 0

print(old)