import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.path import Path
filename="Pearce_Y-Nb.json"

with open(filename,"r") as f:
    y=json.load(f)
dic=y["polygons"]
for key in dic.keys():
    if(key=="VAG+syn-COLG"):
        list=dic[key]
        pgPoints=[]
        for i in range(0,len(list)):
            xp=(np.log10(list[i][0]))
            yp= np.log10(list[i][1])
            pgPoints.append((xp,yp))
        p=Path(pgPoints)
#check position array
p.contains_points([(2, 0.5),(50,25),(2.5,1),(1,2.5)])
#check one position
# p.contains_point((1,2.5))