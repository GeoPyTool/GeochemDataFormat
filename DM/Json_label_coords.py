import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = "Pearce_Y-Nb.json"

with open(filename, "r") as f:
    y = json.load(f)
dic = y["label_coords"]
for key in dic.keys():
    print(key)
    xp = np.log10(dic[key][0])
    yp = np.log10(dic[key][1])
    plt.scatter(xp, yp, s=20, c='b')
    # without arrow
    #     plt.annotate(text=key,xy=(xp,yp),xytext=(xp+0.05,yp+0.05))
    # with arrow
    plt.annotate(text=key, xy=(xp, yp), xytext=(xp + 0.1, yp + 0.1),
                 #                  weight='bold',
                 color='black',
                 arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3', color='red'))
