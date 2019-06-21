#Example 1
# When Data contains scalar values
import pandas as pd
Data = [1, 3, 4, 5, 6, 2, 9]  # Numeric data

# Creating series with default index values
s = pd.Series(Data)

# predefined index values
Index = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Creating series with predefined index values
si = pd.Series(Data, Index)
print(s, si)

#Example2
# When Data contains Dictionary
# Program to Create Dictionary series
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Creating series of Dictionary type
sd = pd.Series(dictionary)
print(sd)

#Example3
#DataFrames:
#DataFrames is two-dimensional(2-D) data structure defined in pandas which consists of rows and columns.
#Here, Data can be:
#One or more dictionaries
#One or more Series
#2D-numpy Ndarray

# Program to Create Data Frame with two dictionaries, when data is dictionary
dict1 ={'a':1, 'b':2, 'c':3, 'd':4}	 # Define Dictionary 1
dict2 ={'a':5, 'b':6, 'c':7, 'd':8, 'e':9} # Define Dictionary 2
Data = {'first':dict1, 'second':dict2} # Define Data with dict1 and dict2
df = pd.DataFrame(Data) # Create DataFrame

# When data is series
# Program to create Dataframe of three series
import pandas as pd

s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])		 # Define series 1
s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3]) # Define series 2
s3 = pd.Series(['a', 'b', 'c', 'd', 'e'])	 # Define series 3


Data ={'first':s1, 'second':s2, 'third':s3} # Define Data
dfseries = pd.DataFrame(Data)			 # Create DataFrame

## Program to create DataFrame from 2D array
#IMPORTANT - One constraint has to be maintained while creating DataFrame of 2D arrays – Dimensions of 2D array must be same.
import pandas as pd # Import Library
d1 =[[2, 3, 4], [5, 6, 7]] # Define 2d array 1
d2 =[[2, 4, 8], [1, 3, 9]] # Define 2d array 2
Data ={'first': d1, 'second': d2} # Define Data
df2d = pd.DataFrame(Data) # Create DataFrame


