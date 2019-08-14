
import pandas as pd
import matplotlib.pyplot as plt
import sys  
import re
import networkx as nx
import numpy as np

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

data = []

for x in range(2,11):
    file1 = 'scenario1/volume' + str(x) +  '-0/events.xml'
    events = pd.read_csv(file1, sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])
    data.append([events['total_time'].mean()])
       
df = pd.DataFrame(data, columns = ['mean_travel']) 
        
print(df['mean_travel'].mean())
print(df['mean_travel'].std())

for y in range(0,11):


    for x in range(0,21):

        data_int = []
        data_int_dr = []
        data_int_non = []
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

    for x in range(0,21):

        data_int = []
        data_int_dr = []
        data_int_non = []
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


    for x in range(0,21):

        data_int = []
        data_int_dr = []
        data_int_non = []
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


    for x in range(0,21):

        data_int = []
        data_int_dr = []
        data_int_non = []
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

print(df2)

df3 = pd.DataFrame(data3, columns = ['scenario', 'mean_travel']) 
df3 = pd.concat([df3.groupby(['scenario']).mean(), df3.groupby(['scenario']).std()], axis=1)
df3 = df3.reset_index()
df3.columns = ['scenario','mean_travel', 'std_travel']

print(df3)

df4 = pd.DataFrame(data4, columns = ['scenario', 'mean_travel']) 
df4 = pd.concat([df4.groupby(['scenario']).mean(), df4.groupby(['scenario']).std()], axis=1)
df4 = df4.reset_index()
df4.columns = ['scenario','mean_travel', 'std_travel']

print(df4)

df5 = pd.DataFrame(data5, columns = ['scenario', 'mean_travel']) 
df5 = pd.concat([df5.groupby(['scenario']).mean(), df5.groupby(['scenario']).std()], axis=1)
df5 = df5.reset_index()
df5.columns = ['scenario','mean_travel', 'std_travel']

print(df5)

ax = df2.plot(
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Mean Travel Time for all Vehicles',
    grid=True,
)

ax = df3.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Mean Travel Time for all Vehicles',
    grid=True,
)

ax = df4.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Mean Travel Time for all Vehicles',
    grid=True,
)

ax = df5.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Mean Travel Time for all Vehicles',
    grid=True,
)

cet_mean = 850
cet_std = 53

ax.hlines(y=cet_mean, xmin=0, xmax=100)
ax.hlines(y=[cet_mean+2*cet_std, cet_mean-2*cet_std], xmin=0, xmax=100, linestyle='--')

ax.legend(['Mean, no AVs', 'STD, no AVs', 'Mean, Scenario 2', 'Mean, Scenario 3', 'Mean, Scenario 4', 'Mean, Scenario 5'])
ax.set_xlabel("AV ratio")
ax.set_ylabel("Travel Time (s)")

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
    title='Mean Travel Time for all Vehicles',
    grid=True,
)

ax = df3.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Mean Travel Time for all Vehicles',
    grid=True,
)

ax = df4.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Mean Travel Time for all Vehicles',
    grid=True,
)

ax = df5.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Mean Travel Time for all Vehicles',
    grid=True,
)


ax.hlines(y=cet_mean, xmin=0, xmax=100)
ax.hlines(y=[cet_mean+2*cet_std, cet_mean-2*cet_std], xmin=0, xmax=100, linestyle='--')

ax.legend(['Mean, no AVs', 'STD CI, no AVs', 'Mean, Scenario 2', 'Mean, Scenario 3', 'Mean, Scenario 4', 'Mean, Scenario 5'])
ax.set_xlabel("AV ratio")
ax.set_ylabel("Travel Time (s)")

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
    title='Mean Travel Time for all Vehicles',
    grid=True,
)

ax = df3.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Mean Travel Time for all Vehicles',
    grid=True,
)


ax = df4.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Mean Travel Time for all Vehicles',
    grid=True,
)

ax = df5.plot(ax=ax,
    x='scenario',
    y='mean_travel',
    marker='o', 
    yerr='std_travel',
    ylim=(0, None),
    title='Mean Travel Time for all Vehicles',
    grid=True,
)

ax.hlines(y=cet_mean, xmin=0, xmax=100)
ax.hlines(y=[cet_mean+2*cet_std, cet_mean-2*cet_std], xmin=0, xmax=100, linestyle='--')

ax.legend(['Mean, no AVs', 'STD, no AVs', 'Mean, Scenario 2', 'Mean, Scenario 3', 'Mean, Scenario 4', 'Mean, Scenario 5'])
ax.set_xlabel("AV ratio")
ax.set_ylabel("Travel Time (s)")

plt.savefig("results/non_dr.png", bbox_inches='tight', pad_inches=0.0)
plt.close()