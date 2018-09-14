"""
QUTIC Crash Course Python

This file will contain the classes and functions
used to calculate the indicators.

Andrew Collison 14-09-18
"""
# Import the modules we need
import pandas as pd
import numpy as np

# Load the data into a pandas data frame
print('hello')
data = pd.read_csv("pair_data.csv", parse_dates = True)
print(data)
print (type(data), data.shape)
print (data.info())


## Create the class to hold the functions
class indicators():
	# Define the functions for the desired indicators
	# Moving Average
	def moving_average(data, window):
		MA = data['Close'].rolling(center = False, window = window).mean()
		name = 'MA' + str(window)
		data['name'] = MA
		return data





	# Keltner Channel


# data = indicators.moving_average(data, 20)
# data = indicators.moving_average(data, 200)
# data = indicators.keltner(data)
# print(data)
data = indicators.moving_average(data, 20)
print(data)
data = indicators.moving_average(data, 20)
print(data.info())

### We will save this file for later
# data.to_csv('indicator_data.csv')
