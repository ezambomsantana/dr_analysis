
import pandas as pd
import matplotlib.pyplot as plt
import sys  
import re
import networkx as nx
import numpy as np
from sklearn.linear_model import LinearRegression

data2 = []
data3 = []
data4 = []

data_dr2 = []
data_dr3 = []
data_dr4 = []

data_non_dr2 = []
data_non_dr3 = []
data_non_dr4 = []

for x in range(0,21):
    file1 = 'scenario2/volume' + str(x) + '/events.xml'
    events = pd.read_csv(file1, sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])
    data2.append([x * 5, events['total_time'].mean(), events['total_time'].std()/8])

    events_dr = events[events['car'].str.contains("dr")] 
    events_non_dr = events[~events['car'].str.contains("dr")] 
    
    data_dr2.append([x * 5, events_dr['total_time'].mean(), events_dr['total_time'].std()/8])
    data_non_dr2.append([x * 5, events_non_dr['total_time'].mean(), events_non_dr['total_time'].std()/8])



for x in range(0,21):
    file1 = 'scenario3/volume' + str(x) + '/events.xml'
    events = pd.read_csv(file1, sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])
    data3.append([x * 5, events['total_time'].mean(), events['total_time'].std()/8])    

    events_dr = events[events['car'].str.contains("dr")] 
    events_non_dr = events[~events['car'].str.contains("dr")] 
    
    data_dr3.append([x * 5, events_dr['total_time'].mean(), events_dr['total_time'].std()/8])
    data_non_dr3.append([x * 5, events_non_dr['total_time'].mean(), events_non_dr['total_time'].std()/8])

for x in range(0,21):
    file1 = 'scenario4/volume' + str(x) + '/events.xml'
    events = pd.read_csv(file1, sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])
    data4.append([x * 5, events['total_time'].mean(), events['total_time'].std()/8])    

    events_dr = events[events['car'].str.contains("dr")] 
    events_non_dr = events[~events['car'].str.contains("dr")] 
    
    data_dr4.append([x * 5, events_dr['total_time'].mean(), events_dr['total_time'].std()/8])
    data_non_dr4.append([x * 5, events_non_dr['total_time'].mean(), events_non_dr['total_time'].std()/8])

df2 = pd.DataFrame(data2, columns = ['scenario', 'mean_travel', 'std_travel']) 
df3 = pd.DataFrame(data3, columns = ['scenario', 'mean_travel', 'std_travel']) 
df4 = pd.DataFrame(data4, columns = ['scenario', 'mean_travel', 'std_travel']) 

ax = df2.plot(
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. AV ratio (%)',
    grid=True,
)

ax = df3.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. AV ratio (%)',
    grid=True,
)

ax = df4.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. AV ratio (%)',
    grid=True,
)

cet_mean = 662
cet_std = 25

ax.hlines(y=cet_mean, xmin=0, xmax=100)
ax.hlines(y=[cet_mean+2*cet_std, cet_mean-2*cet_std], xmin=0, xmax=100, linestyle='--')

ax.legend(['Mean, no DR', '95% CI, no DR', 'Mean, Scenario 2', 'Mean Scenario 3', 'Mean Scenario 4'])

plt.savefig("results/total.png", bbox_inches='tight', pad_inches=0.0)
plt.close()


df2 = pd.DataFrame(data_dr2, columns = ['scenario', 'mean_travel', 'std_travel']) 
df3 = pd.DataFrame(data_dr3, columns = ['scenario', 'mean_travel', 'std_travel']) 
df4 = pd.DataFrame(data_dr4, columns = ['scenario', 'mean_travel', 'std_travel']) 

ax = df2.plot(
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. AV ratio (%)',
    grid=True,
)

ax = df3.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. AV ratio (%)',
    grid=True,
)

ax = df4.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. AV ratio (%)',
    grid=True,
)

cet_mean = 662
cet_std = 25

ax.hlines(y=cet_mean, xmin=0, xmax=100)
ax.hlines(y=[cet_mean+2*cet_std, cet_mean-2*cet_std], xmin=0, xmax=100, linestyle='--')

ax.legend(['Mean, no DR', '95% CI, no DR', 'Mean, Scenario 2', 'Mean Scenario 3', 'Mean Scenario 4'])

plt.savefig("results/dr.png", bbox_inches='tight', pad_inches=0.0)
plt.close()



df2 = pd.DataFrame(data_non_dr2, columns = ['scenario', 'mean_travel', 'std_travel']) 
df3 = pd.DataFrame(data_non_dr3, columns = ['scenario', 'mean_travel', 'std_travel']) 
df4 = pd.DataFrame(data_non_dr3, columns = ['scenario', 'mean_travel', 'std_travel']) 

ax = df2.plot(
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. AV ratio (%)',
    grid=True,
)

ax = df3.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. AV ratio (%)',
    grid=True,
)


ax = df4.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. AV ratio (%)',
    grid=True,
)

cet_mean = 662
cet_std = 25

ax.hlines(y=cet_mean, xmin=0, xmax=100)
ax.hlines(y=[cet_mean+2*cet_std, cet_mean-2*cet_std], xmin=0, xmax=100, linestyle='--')

ax.legend(['Mean, no DR', '95% CI, no DR', 'Mean, Scenario 2', 'Mean Scenario 3', 'Mean Scenario 4'])
plt.savefig("results/non_dr.png", bbox_inches='tight', pad_inches=0.0)
plt.close()