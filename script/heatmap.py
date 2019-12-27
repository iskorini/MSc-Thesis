import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path
import os

labels = ['person', 'people']
path_csv = Path('/Users/fschipani/Desktop/Tesi/MSc-Thesis-PJ/Dataset/KAIST_MPD/imageSets/csv_files/lwir/')
ds = pd.DataFrame(None, columns=[0,1,2,3,4,5])
for file in os.listdir(path_csv):
    csv_file = pd.read_csv(path_csv.joinpath(file), header=None)
    csv_file = csv_file.loc[csv_file[5].isin(labels)]
    ds = pd.concat([ds, csv_file])
heatmap = np.zeros([512, 640], dtype=np.int)
for index, row in ds.iterrows():
    (x_min, y_min) = int(row[1]), int(row[2]) 
    (x_max, y_max) = int(row[3]), int(row[4])
    heatmap[y_min:y_max, x_min:x_max]+=1
plt.imshow(heatmap, cmap='plasma', interpolation='nearest')
plt.savefig('./heatmap.pdf', format='pdf')
#plt.show(sb.heatmap(heatmap, xticklabels=False, yticklabels=False))