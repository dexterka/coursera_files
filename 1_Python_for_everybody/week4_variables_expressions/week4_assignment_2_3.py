# user's input
hrs = input("Enter the number of hours:")
rate = input("Enter the rate per hour:")

# convert strings to numbers
hours_converted = float(hrs)
rate_converted = float(rate)

# calculate and print the salary
pay = hours_converted * rate_converted

print("Pay:", pay)