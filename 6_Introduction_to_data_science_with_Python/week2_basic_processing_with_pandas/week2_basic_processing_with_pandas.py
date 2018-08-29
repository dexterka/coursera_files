# Env setup
import pandas as pd
import numpy as np

# List of all items
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
# print(df['Item Purchased'].to_string(index = False))

# Apply a discount of 20% to all values in the cost column
# df['Cost'] *= 0.8  # broadcasting
# print(df)

# Write a query to return all of the names of people who bought products worth more than $3.00.
# more_than_3 = df[df['Cost'] > 3]
# print(more_than_3['Name'])
# print(df['Name'][df['Cost'] > 3])

# Reindex the purchase records DataFrame to be indexed hierarchically, first by store, then by person.
#  Name these indexes 'Location' and 'Name'. Then add a new entry to it with the value of:
# Name: 'Kevyn', Item Purchased: 'Kitty Food', Cost: 3.00 Location: 'Store 2'.
df['Location'] = df.index
df = df.set_index(['Location', 'Name'])
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))
print(df)