# Define the function for the calculation
def computepay(hours, rate):
    if hours <= 40:
       return hours * rate
    else:
        return 40 * rate + (hours - 40) * (1.5 * rate)


# User's input
hours = float(input('Enter the number of hours:'))
rate = float(input('Enter the rate per hour:'))

# Compute the salary
salary = computepay(hours, rate)
print(salary)