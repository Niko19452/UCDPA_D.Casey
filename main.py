# Project for Certificate in Data Analytics for Marketing
# Student Name: Dominic Casey Student ID: E10617514
# 1) Real-world dataset. 'All residential properties sold in Ireland from 2010 to May 28th 2021’ downloaded csv file from kaggle.com

# import the Pandas liberies as pd
import plistlib

import pandas as pd

# import NmmPy liberies as np
import numpy as np

# import Matplotlib which is a plotting library for the Python programming language and its numerical mathematics extension NumPy
import matplotlib.pyplot as plt

# import Geopandas to plot results on the map of Ireland.
import geopandas as gpd

# 2) Importing the data. load the dataset. 'All residential properties sold in Ireland from 2010 to May 28th 2021’ downloaded from kaggle.com
df = pd.read_csv("/Users/dominiccasey/PycharmProjects/Source Files/Property_Price_Register_Ireland-28-05-2021.csv")
df

# 3) Analysising the data. Check the first 5 rows of the dataset and view header names
print (df.head())
print (df.head(0))

# Postal codes are unique therefore check the postal code to elimate duplicates. True get converted to 1 and False get converted to 0
df.duplicated('POSTAL_CODE').sum()

# iterrows and merging
# define a smaller datafram df1
df1 = pd.DataFrame(df)
df1.iloc[0]

# display VAT Excluded purchases for Cork
# loc() is a label based data selecting and includes the last element of range passed to it
df2=(df.loc[df.COUNTY == 'Cork'])
df3 = (df2.loc[ df.IF_VAT_EXCLUDED==1])
print (df3)












