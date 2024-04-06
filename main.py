import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

auto_data = pd.read_csv("Automobile_data.csv")
print(auto_data.head())
print(auto_data.info())

#1) handle missing values for price

auto_data['price'] = auto_data['price'].replace('?', np.nan)
auto_data['price'] = auto_data['price'].astype(float)
auto_data['price'] = auto_data['price'].fillna(auto_data['price'].mean())
print(auto_data['price'])
#checking if the missing values have been replaced
print(auto_data['price'].isnull().sum())

#2)Get the values from price column into a numpy nd array
price = auto_data['price'].values
print(price)

#3)Calculating minimum,maximum,average, and standard deviation of the price
print("Minimum price:", np.min(price))
print("Maximum price:", np.max(price))
print("Average price:", np.mean(price))