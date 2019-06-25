
import pandas as pd
import matplotlib.pyplot as plt
import sys  
import re
import networkx as nx
import numpy as np
from sklearn.linear_model import LinearRegression

events = pd.read_csv('events.csv', sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])

events['real_minute'] = pd.to_numeric(events['real_minute'])
events['total_time'] = pd.to_numeric(events['total_time'])
events['inicio'] = events['real_minute'] - events['total_time']

count_cars = []
value = 200
for x in range(1, 25):
    inte = value * x
    count = 0
    for index, row in events.iterrows():
        if row['inicio'] < inte and row['total_time'] + row['inicio'] > inte:
            count = count + 1
    count_cars.append([inte, count])

bins = []
names = []
bins.append(0)
for x in range(1, 50):
    bins.append(x * 100)
    names.append(str((x-1)*100))
    
events['interval'] = pd.cut(events['real_minute'], bins, labels=names)

events_mean = events.groupby(['interval']).mean()
events_mean = events_mean.reset_index()

events_mean = events_mean[['interval', 'total_time']].dropna()
events_mean.plot.line(x='interval', y='total_time')
plt.show()

par = events[events['car'].str.contains("paraiso")]
cons = events[events['car'].str.contains("consolacao")]

print(par['interval'].size)
print(cons['interval'].size)

par['interval'] = pd.to_numeric(par['interval'])
par.plot.scatter(x='interval', y='total_time')
plt.show()

cons['interval'] = pd.to_numeric(cons['interval'])
cons.plot.scatter(x='interval', y='total_time')
plt.show()