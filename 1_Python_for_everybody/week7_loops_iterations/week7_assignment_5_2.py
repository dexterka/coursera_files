# Find the smallest and largest value from user's input
min_number = None
max_number = None

while True:
    user_input = input('Enter an integer number:')

    if user_input == 'done':
        break
        # print(user_input)

    # Deal with the invalid user's input
    try:
        user_input_num = int(user_input)
    except:
        print('Invalid input')
        continue

    # Smallest value
    if min_number is None:
        min_number = user_input_num
    elif user_input_num < min_number:
        min_number = user_input_num

    # Largest value
    if max_number is None:
        max_number = user_input_num
    elif user_input_num > max_number:
        max_number = user_input_num

print('Maximum is', max_number)
print('Minimum is', min_number)
