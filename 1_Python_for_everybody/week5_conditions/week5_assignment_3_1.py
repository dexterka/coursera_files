# User's input
hours = input('Enter the number of hours:')
rate = input('Enter your hourly rate:')

# Convert to floating numbers
hours_num  = float(hours)
rate_num = float(rate)

# Calculate the salary
if hours_num <= 40:
    salary = hours_num * rate_num
else:
    salary = 40 * rate_num + (hours_num - 40) * (1.5 * rate_num)

print(salary)
# print('Your salary is:', salary)
