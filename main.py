# Project for Certificate in Data Analytics for Marketing
# Student Name: Dominic Casey Student ID: E10617514
# Dataset 'All residential properties sold in Ireland from 2010 to May 28th 2021’ downloaded from kaggle.com

import pandas as pd
# load the dataset
data = pd.read_csv("/Users/dominiccasey/PycharmProjects/Source Files/Property_Price_Register_Ireland-28-05-2021.csv")
# Preview the first 5 lines of the loaded data
data.head()

print(data)