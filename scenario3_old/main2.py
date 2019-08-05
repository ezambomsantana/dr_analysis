
import pandas as pd
import matplotlib.pyplot as plt
import sys  
import re
import networkx as nx
import numpy as np
from sklearn.linear_model import LinearRegression

data = []

for x in range(0,21):
    file1 = 'volume' + str(x) + '/events.xml'
    print(file1)
    events = pd.read_csv(file1, sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])

    print(events['total_time'].mean())

    data.append([x * 5, events['total_time'].mean(), events['total_time'].std()/10])

df = pd.DataFrame(data, columns = ['scenario', 'mean_travel', 'std_travel']) 
df.mean_travel = df.mean_travel.astype(int)
df.std_travel = df.std_travel.astype(int)
df.scenario = df.scenario.astype(int)
print(df)



ax = df.plot(
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

ax.legend(['Mean, no DR', '95% CI, no DR', 'Mean, DR'])
plt.show()