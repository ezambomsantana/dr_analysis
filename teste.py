

import pandas as pd
import matplotlib.pyplot as plt
import sys  
import re
import networkx as nx
import numpy as np
from sklearn.linear_model import LinearRegression

data_int = []
data_int_dr = []
data_int_non = []
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

x = 20

file1 = 'scenario5/volume0-20/events.xml'
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

print(data5)
print(data_dr5)
print(data_non_dr5)