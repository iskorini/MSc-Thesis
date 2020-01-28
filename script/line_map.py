import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set(style='whitegrid', palette='Set2')

def annot_max(x,y, xytext=None, angleB = 120, ax=None):
    xmax = x[np.argmax(y)]
    ymax = y.max()
    text= "epoch={:0d}, map={:.4f}".format(xmax, ymax)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="round,pad=0.3", fc="w", ec="k", lw=1)
    arrowprops=dict(color='black', arrowstyle="->",connectionstyle="angle,angleA=0,angleB="+str(angleB))
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="bottom")
    ax.annotate(text, xy=(xmax, ymax), xytext=xytext, **kw)


csv_path = '/Users/fschipani/Desktop/evaluation_CAR_RA.csv'
dataframe = pd.read_csv(csv_path)[['epoch', 'map_person', 'map_cars', 'map_cyclist', 'map']].sort_values(by='epoch')

ax = plt.gca()
#ax.set_aspect(20)

dataframe.plot(x='epoch', y=['map_person', 'map_cars', 'map_cyclist'], ax = ax)
plt.legend(ncol=1, loc='upper right');
ax.yaxis.grid(True) 
ax.xaxis.grid(False)
ax.margins()
ax.set_ylim(bottom=0)
ax.set_ylabel('map')
sns.despine()
#plt.show()
annot_max(dataframe['epoch'], dataframe['map_person'], xytext=(0.94,0.2))
annot_max(dataframe['epoch'], dataframe['map_cars'], xytext=(0.94,0.3))
annot_max(dataframe['epoch'], dataframe['map_cyclist'], xytext=(0.94,0.4), angleB=60)
#annot_max(dataframe['epoch'], dataframe['map_cars'])
plt.savefig('./graphics.pdf', format='pdf', bbox_inches='tight')