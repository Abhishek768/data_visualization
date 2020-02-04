# importing numpy and pandas module
from numpy.random import randn
import pandas as pd

# variables 
my_index = ['A', 'B', 'C', 'D', 'E']
my_column = [1, 2, 3, 4]

# data frames of pandas have similar representation as Excel
df = pd.DataFrame(randn(5,4), my_index, my_column)

# conditional selection in datat= frames
print(df[(df[1] > 0) & (df[2] > 0)])	

# to set an index 

new_index = 'IN RS PS CS DS'.split()

df['new'] = new_index
df.set_index('new') #, inplace = true ) to set index permanently

print(df) 