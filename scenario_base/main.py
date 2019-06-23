
import pandas as pd
import matplotlib.pyplot as plt
import sys  
import re
import networkx as nx
import numpy as np
from sklearn.linear_model import LinearRegression

events = pd.read_csv('events.csv', sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])

bins = []
names = []

bins.append(0)
for x in range(1, 50):
    bins.append(x * 100)
    names.append(str((x-1)*100))

print(events)
    
events['interval'] = pd.cut(events['real_minute'], bins, labels=names)

events_mean = events.groupby(['interval']).mean()
events_mean = events_mean.reset_index()

events_mean = events_mean[['interval', 'total_time']].dropna()
events_mean.plot.line(x='interval', y='total_time')
plt.show()


X = events_mean.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
Y = events_mean.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions

plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.show()