# importing numpy and pandas module
import numpy as np
import pandas as pd

# variables
my_list = [1, 2, 3]
labels = ['IND', 'USA', 'CAD']

# series1
ser1 = pd.Series(my_list, labels)

# series2
ser2 = pd.Series([1, 2, 4], ['IND', 'USA', 'ENG'])

# addition of two pandas series
result = ser1 + ser2

# will drop null values from series
print(result.dropna())