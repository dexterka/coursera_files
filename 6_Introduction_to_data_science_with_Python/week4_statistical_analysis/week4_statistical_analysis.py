import pandas as pd
import numpy as np

# Suppose we want to simulate the probability of flipping a fair coin 20 times, and getting a number greater than
#  or equal to 15. Use np.random.binomial(n, p, size) to do 10000 simulations of flipping a fair coin 20 times,
#  then see what proportion of the simulations are 15 or greater.
x = np.random.binomial(20, .5, 10000)
print((x >= 15).mean())  # 2.31%

print(type(lambda x: x+1))