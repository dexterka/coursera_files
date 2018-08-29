# Extract the mail addresses from file
file_name = input('Enter the name of the file: ')
file_read = open(file_name, 'r')

count = 0

for line in file_read:
    if not line.startswith('From:'):
        if line.startswith('From'):
            line = line.rstrip()
            words = line.split()
            mail_address = words[1]
            count = count + 1
            print(mail_address)

print('There were %d lines in the file with From as the first word' % count)