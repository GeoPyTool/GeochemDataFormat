import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
filename='Pearce_Y-Nb.json'

with open(filename,"r") as f:
    y=json.load(f)
dic=y["lines"]

for key in dic.keys():
    x_list=[]
    y_list=[]
#     print(dic[key][0],dic[key][1])
    list=dic[key]
    for i in range(0,len(list)):
        x_list.append(np.log10(list[i][0]))
        y_list.append(np.log10(list[i][1]))
    plt.plot(x_list,y_list,linewidth=1, color='red')

