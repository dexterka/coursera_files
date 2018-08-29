import pandas as pd
import numpy as np

# Group by category and calculate the total weight across categories
print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))

# Try casting this series to categorical with the ordering Low < Medium < High.
s.astype('category', categories = ['Low', 'Medium', 'High'], ordered = True)


# Suppose we have a series that holds height data for jacket wearers. Use pd.cut to bin this data into 3 bins.
s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])
print(pd.cut(s, 3))
# You can also add labels for the sizes [Small < Medium < Large].
print(pd.cut(s, 3, labels=['Small', 'Medium', 'Large']))

# Create a pivot table that shows the mean price and mean rating for every 'Manufacturer' / 'Bike Type' combination.
Bikes.pivot_table(values = ('Price', 'Rating'), index = 'Bike Type', columns = 'Manufacturer', aggfunc = np.mean)
print(pd.pivot_table(Bikes, index=['Manufacturer','Bike Type']))