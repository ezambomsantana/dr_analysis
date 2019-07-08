
import pandas as pd
import matplotlib.pyplot as plt
import sys  
import re
import networkx as nx
import numpy as np
from sklearn.linear_model import LinearRegression


for x in range(0,21):
    file1 = 'volume' + str(x) + '/events.xml'
    print(file1)
    events = pd.read_csv(file1, sep = ';', header=None, names=['real_hour', 'real_minute', 'time','car', 'final_link', 'total_time','total_distance'])

    print(events['total_time'].mean())
