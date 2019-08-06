
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
data5 = []

data_dr2 = []
data_dr3 = []
data_dr4 = []
data_dr5 = []

data_non_dr2 = []
data_non_dr3 = []
data_non_dr4 = []
data_non_dr5 = []

for y in range(0,11):

    data_int = []
    data_int_dr = []
    data_int_non = []

    for x in range(0,21):
        file1 = 'scenario2/volume' + str(y) + '-' + str(x) + '/events.xml'
        events = pd.read_csv(file1, sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])
        data_int.append([x * 5, events['total_time'].mean()])

        events_dr = events[events['car'].str.contains("dr")] 
        events_non_dr = events[~events['car'].str.contains("dr")] 
        
        data_int_dr.append([x * 5, events_dr['total_time'].mean()])
        data_int_non.append([x * 5, events_non_dr['total_time'].mean()])
       
        df_int = pd.DataFrame(data_int, columns = ['scenario','mean_travel'])  
        df_int_dr = pd.DataFrame(data_int_dr, columns = ['scenario','mean_travel']) 
        df_int_non = pd.DataFrame(data_int_non, columns = ['scenario','mean_travel']) 
        
        data2.append([x * 5, df_int['mean_travel'].mean()])
        data_dr2.append([x * 5, df_int_dr['mean_travel'].mean()])
        data_non_dr2.append([x * 5, df_int_non['mean_travel'].mean()])


for y in range(0,11):

    data_int = []
    data_int_dr = []
    data_int_non = []

    for x in range(0,21):
        file1 = 'scenario3/volume' + str(y) + '-' + str(x) + '/events.xml'
        events = pd.read_csv(file1, sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])
        data_int.append([x * 5, events['total_time'].mean()])

        events_dr = events[events['car'].str.contains("dr")] 
        events_non_dr = events[~events['car'].str.contains("dr")] 
        
        data_int_dr.append([x * 5, events_dr['total_time'].mean()])
        data_int_non.append([x * 5, events_non_dr['total_time'].mean()])
       
        df_int = pd.DataFrame(data_int, columns = ['scenario','mean_travel'])  
        df_int_dr = pd.DataFrame(data_int_dr, columns = ['scenario','mean_travel']) 
        df_int_non = pd.DataFrame(data_int_non, columns = ['scenario','mean_travel']) 
        
        data3.append([x * 5, df_int['mean_travel'].mean()])
        data_dr3.append([x * 5, df_int_dr['mean_travel'].mean()])
        data_non_dr3.append([x * 5, df_int_non['mean_travel'].mean()])

for y in range(0,11):

    data_int = []
    data_int_dr = []
    data_int_non = []

    for x in range(0,21):
        file1 = 'scenario4/volume' + str(y) + '-' + str(x) + '/events.xml'
        events = pd.read_csv(file1, sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])
        data_int.append([x * 5, events['total_time'].mean()])

        events_dr = events[events['car'].str.contains("dr")] 
        events_non_dr = events[~events['car'].str.contains("dr")] 
        
        data_int_dr.append([x * 5, events_dr['total_time'].mean()])
        data_int_non.append([x * 5, events_non_dr['total_time'].mean()])
       
        df_int = pd.DataFrame(data_int, columns = ['scenario','mean_travel'])  
        df_int_dr = pd.DataFrame(data_int_dr, columns = ['scenario','mean_travel']) 
        df_int_non = pd.DataFrame(data_int_non, columns = ['scenario','mean_travel']) 
        
        data4.append([x * 5, df_int['mean_travel'].mean()])
        data_dr4.append([x * 5, df_int_dr['mean_travel'].mean()])
        data_non_dr4.append([x * 5, df_int_non['mean_travel'].mean()])

for y in range(0,11):

    data_int = []
    data_int_dr = []
    data_int_non = []

    for x in range(0,21):
        file1 = 'scenario5/volume' + str(y) + '-' + str(x) + '/events.xml'
        events = pd.read_csv(file1, sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])
        data_int.append([x * 5, events['total_time'].mean()])

        events_dr = events[events['car'].str.contains("dr")] 
        events_non_dr = events[~events['car'].str.contains("dr")] 
        
        data_int_dr.append([x * 5, events_dr['total_time'].mean()])
        data_int_non.append([x * 5, events_non_dr['total_time'].mean()])
       
        df_int = pd.DataFrame(data_int, columns = ['scenario','mean_travel'])  
        df_int_dr = pd.DataFrame(data_int_dr, columns = ['scenario','mean_travel']) 
        df_int_non = pd.DataFrame(data_int_non, columns = ['scenario','mean_travel']) 
        
        data5.append([x * 5, df_int['mean_travel'].mean()])
        data_dr5.append([x * 5, df_int_dr['mean_travel'].mean()])
        data_non_dr5.append([x * 5, df_int_non['mean_travel'].mean()])



df2 = pd.DataFrame(data2, columns = ['scenario', 'mean_travel']) 
df2 = pd.concat([df2.groupby(['scenario']).mean(), df2.groupby(['scenario']).std()], axis=1)
df2 = df2.reset_index()
df2.columns = ['scenario','mean_travel', 'std_travel']


df3 = pd.DataFrame(data3, columns = ['scenario', 'mean_travel']) 
df3 = pd.concat([df3.groupby(['scenario']).mean(), df3.groupby(['scenario']).std()], axis=1)
df3 = df3.reset_index()
df3.columns = ['scenario','mean_travel', 'std_travel']


df4 = pd.DataFrame(data4, columns = ['scenario', 'mean_travel']) 
df4 = pd.concat([df4.groupby(['scenario']).mean(), df4.groupby(['scenario']).std()], axis=1)
df4 = df4.reset_index()
df4.columns = ['scenario','mean_travel', 'std_travel']


df5 = pd.DataFrame(data5, columns = ['scenario', 'mean_travel']) 
df5 = pd.concat([df5.groupby(['scenario']).mean(), df5.groupby(['scenario']).std()], axis=1)
df5 = df5.reset_index()
df5.columns = ['scenario','mean_travel', 'std_travel']

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

ax = df5.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. AV ratio (%)',
    grid=True,
)

cet_mean = 810
cet_std = 25

ax.hlines(y=cet_mean, xmin=0, xmax=100)
ax.hlines(y=[cet_mean+2*cet_std, cet_mean-2*cet_std], xmin=0, xmax=100, linestyle='--')

ax.legend(['Mean, no DR', '95% CI, no DR', 'Mean, Scenario 2', 'Mean Scenario 3', 'Mean Scenario 4', 'Mean Scenario 5'])

plt.savefig("results/total.png", bbox_inches='tight', pad_inches=0.0)
plt.close()

df2 = pd.DataFrame(data_dr2, columns = ['scenario', 'mean_travel']) 
df2 = pd.concat([df2.groupby(['scenario']).mean(), df2.groupby(['scenario']).std()], axis=1)
df2 = df2.reset_index()
df2.columns = ['scenario','mean_travel', 'std_travel']


df3 = pd.DataFrame(data_dr3, columns = ['scenario', 'mean_travel']) 
df3 = pd.concat([df3.groupby(['scenario']).mean(), df3.groupby(['scenario']).std()], axis=1)
df3 = df3.reset_index()
df3.columns = ['scenario','mean_travel', 'std_travel']


df4 = pd.DataFrame(data_dr4, columns = ['scenario', 'mean_travel']) 
df4 = pd.concat([df4.groupby(['scenario']).mean(), df4.groupby(['scenario']).std()], axis=1)
df4 = df4.reset_index()
df4.columns = ['scenario','mean_travel', 'std_travel']


df5 = pd.DataFrame(data_dr5, columns = ['scenario', 'mean_travel']) 
df5 = pd.concat([df5.groupby(['scenario']).mean(), df5.groupby(['scenario']).std()], axis=1)
df5 = df5.reset_index()
df5.columns = ['scenario','mean_travel', 'std_travel']

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

ax = df5.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. AV ratio (%)',
    grid=True,
)


ax.hlines(y=cet_mean, xmin=0, xmax=100)
ax.hlines(y=[cet_mean+2*cet_std, cet_mean-2*cet_std], xmin=0, xmax=100, linestyle='--')

ax.legend(['Mean, no DR', '95% CI, no DR', 'Mean, Scenario 2', 'Mean Scenario 3', 'Mean Scenario 4', 'Mean Scenario 5'])

plt.savefig("results/dr.png", bbox_inches='tight', pad_inches=0.0)
plt.close()



df2 = pd.DataFrame(data_non_dr2, columns = ['scenario', 'mean_travel']) 
df2 = pd.concat([df2.groupby(['scenario']).mean(), df2.groupby(['scenario']).std()], axis=1)
df2 = df2.reset_index()
df2.columns = ['scenario','mean_travel', 'std_travel']


df3 = pd.DataFrame(data_non_dr3, columns = ['scenario', 'mean_travel']) 
df3 = pd.concat([df3.groupby(['scenario']).mean(), df3.groupby(['scenario']).std()], axis=1)
df3 = df3.reset_index()
df3.columns = ['scenario','mean_travel', 'std_travel']


df4 = pd.DataFrame(data_non_dr4, columns = ['scenario', 'mean_travel']) 
df4 = pd.concat([df4.groupby(['scenario']).mean(), df4.groupby(['scenario']).std()], axis=1)
df4 = df4.reset_index()
df4.columns = ['scenario','mean_travel', 'std_travel']



df5 = pd.DataFrame(data_non_dr5, columns = ['scenario', 'mean_travel']) 
df5 = pd.concat([df5.groupby(['scenario']).mean(), df5.groupby(['scenario']).std()], axis=1)
df5 = df5.reset_index()
df5.columns = ['scenario','mean_travel', 'std_travel']

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

ax = df5.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Travel time (s) vs. AV ratio (%)',
    grid=True,
)

ax.hlines(y=cet_mean, xmin=0, xmax=100)
ax.hlines(y=[cet_mean+2*cet_std, cet_mean-2*cet_std], xmin=0, xmax=100, linestyle='--')

ax.legend(['Mean, no DR', '95% CI, no DR', 'Mean, Scenario 2', 'Mean Scenario 3', 'Mean Scenario 4', 'Mean Scenario 5'])
plt.savefig("results/non_dr.png", bbox_inches='tight', pad_inches=0.0)
plt.close()