import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
filename="Pearce_Y-Nb.json"

with open(filename,"r") as f:
    jsonFile=json.load(f)
for key in jsonFile:
    jsonDic=jsonFile[key]
    if key=="lines":
        for line in jsonDic.keys():
            x_list=[]
            y_list=[]
            line_list=jsonDic[line]
            for i in range(0,len(line_list)):

                x_list.append(np.log10(line_list[i][0]))
                y_list.append(np.log10(line_list[i][1]))
            plt.plot(x_list,y_list,linewidth=1, color='darkgreen',ls="solid")
    if key=="polygons":
        for polygon in jsonDic.keys():
            x_list=[]
            y_list=[]
            polygon_list=jsonDic[polygon]
            for i in range(0,len(polygon_list)):
                x_list.append(np.log10(polygon_list[i][0]))
                y_list.append(np.log10(polygon_list[i][1]))
                if i==len(list)-1:
                    x_list.append(np.log10(polygon_list[0][0]))
                    y_list.append(np.log10(polygon_list[0][1]))
            plt.plot(x_list,y_list,linewidth=1, color='white',ls="solid")
    if key=="label_coords":
        for label_coord in jsonDic.keys():
            xp=np.log10(jsonDic[label_coord][0])
            yp=np.log10(jsonDic[label_coord][1])
            plt.scatter(xp,yp,s=20, c='b')
            plt.annotate(text=key,xy=(xp,yp),xytext=(xp+0.05,yp+0.05))