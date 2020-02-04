# importing numpy and pandas module
import numpy as np
import pandas as pd

# implementing pandas series
my_list = [1, 2, 3]
labels = ['IND', 'USA', 'CAD']

print(pd.Series(my_list, labels))