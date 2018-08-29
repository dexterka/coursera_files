# First input would have caused an error if not handled by try cacth/except
input1 = 'Hello there!'

try:
    output1 = int(input1)
except:
    output1 = 1

print('First input:', output1)

# Second input would have passed even without try catch/except
input2 = '123'

try:
    output2 = int(input2)
except:
    output2 = 1

print('Second input:', output2)

