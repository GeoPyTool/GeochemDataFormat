import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
filename="Pearce_Y-Nb.json"

with open(filename,"r") as f:
    y=json.load(f)
dic=y["polygons"]

for key in dic.keys():
    x_list=[]
    y_list=[]
    list=dic[key]
    for i in range(0,len(list)):
        x_list.append(np.log10(list[i][0]))
        y_list.append(np.log10(list[i][1]))
        if i==len(list)-1:
            x_list.append(np.log10(list[0][0]))
            y_list.append(np.log10(list[0][1]))
    plt.plot(x_list,y_list,linewidth=1, color='mistyrose')