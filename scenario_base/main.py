
import pandas as pd
import matplotlib.pyplot as plt
import sys  
import re
import networkx as nx

events = pd.read_csv('events.csv', sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])

bins = []
names = []

bins.append(0)
for x in range(1, 50):
    bins.append(x * 200)
    names.append(str((x-1)*200))
    
events['interval'] = pd.cut(events['total_time'], bins, labels=names)