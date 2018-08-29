# User's input
score = input('Enter your score:')
score_num = float(score)

# Print the results
if score_num >= 0.9 and score_num <= 1.0:
    print('A')
elif score_num >= 0.8 and score_num < 0.9:
    print('B')
elif score_num >= 0.7 and score_num < 0.8:
    print('C')
elif score_num >= 0.6 and score_num < 0.7:
    print('D')
elif score_num < 0.6 and score_num >= 0.0:
    print('F')
else:
    print('Your score is out of range. Please enter values ranging from 0.0 to 1.0. Thank you.')
