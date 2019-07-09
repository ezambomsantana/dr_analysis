
import pandas as pd
import matplotlib.pyplot as plt
import sys  
import re
import networkx as nx
import numpy as np
from sklearn.linear_model import LinearRegression

data2 = []
data3 = []

for x in range(0,21):
    file1 = 'scenario2/volume' + str(x) + '/events.xml'
    print(file1)
    events = pd.read_csv(file1, sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])

    print(events['total_time'].mean())

    data2.append([x * 5, events['total_time'].mean(), events['total_time'].std()/10])

for x in range(0,21):
    file1 = 'scenario3/volume' + str(x) + '/events.xml'
    print(file1)
    events = pd.read_csv(file1, sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])

    print(events['total_time'].mean())

    data3.append([x * 5, events['total_time'].mean(), events['total_time'].std()/10])    

df2 = pd.DataFrame(data2, columns = ['scenario', 'mean_travel', 'std_travel']) 
df3 = pd.DataFrame(data3, columns = ['scenario', 'mean_travel', 'std_travel']) 

ax = df2.plot(
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. DR ratio (%)',
    grid=True,
)

ax = df3.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. DR ratio (%)',
    grid=True,
)

cet_mean = 662
cet_std = 25

ax.hlines(y=cet_mean, xmin=0, xmax=100)
ax.hlines(y=[cet_mean+2*cet_std, cet_mean-2*cet_std], xmin=0, xmax=100, linestyle='--')

ax.legend(['Mean, no DR', '95% CI, no DR', 'Mean, Scenario 2', 'Mean Scenario 3'])
plt.show()