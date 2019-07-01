
import pandas as pd
import matplotlib.pyplot as plt
import sys  
import re
import networkx as nx
import numpy as np
from sklearn.linear_model import LinearRegression

events = pd.read_csv('events.csv', sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])

print(events['total_time'].mean())

events['real_minute'] = pd.to_numeric(events['real_minute'])
events['total_time'] = pd.to_numeric(events['total_time'])
events['inicio'] = events['real_minute'] - events['total_time']

count_cars = []
count_cars_par = []
count_cars_cons = []
value = 200
for x in range(1, 22):
    inte = value * x
    count = 0
    count_par = 0
    count_cons = 0
    for index, row in events.iterrows():
        if row['inicio'] < inte and row['total_time'] + row['inicio'] > inte:
            count = count + 1
            if "paraiso" in row['car']:
                count_par = count_par + 1
            else:
                count_cons = count_cons + 1
    count_cars.append([inte, count])
    count_cars_par.append([inte, count_par])
    count_cars_cons.append([inte, count_cons])

df = pd.DataFrame(count_cars, columns = ['time', 'count']) 
df.plot.bar(x='time', y='count')
plt.savefig('img/count_cars.png')

df = pd.DataFrame(count_cars_par, columns = ['time', 'count']) 
df.plot.bar(x='time', y='count')
plt.savefig('img/count_cars_par.png')


df = pd.DataFrame(count_cars_cons, columns = ['time', 'count']) 
df.plot.bar(x='time', y='count')
plt.savefig('img/count_cars_cons.png')

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
plt.savefig('img/time.png')

par = events[events['car'].str.contains("paraiso")]
cons = events[events['car'].str.contains("consolacao")]

print(par['interval'].size)
print(cons['interval'].size)

par['interval'] = pd.to_numeric(par['interval'])
par.plot.line(x='interval', y='total_time')
plt.savefig('img/time_par.png')

cons['interval'] = pd.to_numeric(cons['interval'])
cons.plot.line(x='interval', y='total_time')
plt.savefig('img/time_cons.png')

events_mean = par.groupby(['interval']).mean()
events_mean = events_mean.reset_index()

events_mean = events_mean[['interval', 'total_time']].dropna()
events_mean.plot.line(x='interval', y='total_time')
plt.savefig('img/time_par.png')

events_mean = cons.groupby(['interval']).mean()
events_mean = events_mean.reset_index()

events_mean = events_mean[['interval', 'total_time']].dropna()
events_mean.plot.line(x='interval', y='total_time')
plt.savefig('img/time_cons.png')