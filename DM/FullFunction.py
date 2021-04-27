import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.path import Path

filename = "Pearce_Y-Nb.json"

with open(filename, "r") as f:
    y = json.load(f)
axis = y["axis"]
log = y["log"]
# read excel
raw = pd.read_excel("Geochemistry.xlsx")
# from json axis get the colomn
if axis[0] + '(ppm)' in raw.keys():
    a = raw[axis[0] + '(ppm)']
else:
    a = raw[axis[0]]

if axis[1] + '(ppm)' in raw.keys():
    b = raw[axis[1] + '(ppm)']
else:
    b = axis[1]

lablelist = []
for i in range(len(raw)):
    tmp_label = raw.Label[i]
    if tmp_label not in lablelist:
        lablelist.append(tmp_label)
    else:
        lablelist.append('')

for i in range(len(raw)):
    if log:
        x_pos = np.log10([a[i]])
        y_pos = np.log10([b[i]])
    else:
        x_pos = [a[i]]
        y_pos = [b[i]]
    plt.scatter(x_pos, y_pos,
                marker=raw.Marker[i],
                c=raw.Color[i],
                s=raw.Size[i],
                linewidth=raw.Width[i],
                alpha=raw.Alpha[i],
                label=lablelist[i]
                )

plt.legend(loc='best')

plt.xlabel(axis[0])
plt.ylabel(axis[1])
# "=============================================================="
dic = y["lines"]

for key in dic.keys():
    x_list = []
    y_list = []
    list = dic[key]
    for i in range(0, len(list)):
        if log:
            x_list.append(np.log10(list[i][0]))
            y_list.append(np.log10(list[i][1]))
        else:
            x_list.append(list[i][0])
            y_list.append(list[i][1])
    plt.plot(x_list, y_list, linewidth=1, color='darkgreen', ls="solid")
#     =============================================
dic = y["polygons"]

for key in dic.keys():
    x_list = []
    y_list = []
    list = dic[key]
    for i in range(0, len(list)):
        if log:
            x_list.append(np.log10(list[i][0]))
            y_list.append(np.log10(list[i][1]))
            if i == len(list) - 1:
                x_list.append(np.log10(list[0][0]))
                y_list.append(np.log10(list[0][1]))
        else:
            x_list.append(list[i][0])
            y_list.append(list[i][1])
            if i == len(list) - 1:
                x_list.append(list[0][0])
                y_list.append(list[0][1])
    plt.plot(x_list, y_list, linewidth=1, color='white', ls="solid")
#     =============================================

dic = y["label_coords"]
for key in dic.keys():
    if log:
        xp = np.log10(dic[key][0])
        yp = np.log10(dic[key][1])
    else:
        xp = dic[key][0]
        yp = dic[key][1]
    plt.scatter(xp, yp, s=20, c='b')
    plt.annotate(text=key, xy=(xp, yp), xytext=(xp + 0.05, yp + 0.05))
plt.show()