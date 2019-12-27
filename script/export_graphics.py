import wandb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid', palette='Set2')


api = wandb.Api()

# run is specified by <entity>/<project>/<run id>
run = api.run("iskorini/MSc-Thesis-PJ/n9gsww1p")

# save the metrics for the run to a csv file
metrics_dataframe = run.history()
metrics_dataframe.to_csv("metrics.csv")
ax = plt.gca()
ax.set_aspect(20)

metrics_dataframe.plot(x='epoch', y=['classification_loss', 'regression_loss', 'loss'], ax = ax)
#metrics_dataframe.plot(x='epoch', y='classification_loss', ax=ax, color = 'steelblue')
#metrics_dataframe.plot(x='epoch', y='regression_loss', ax=ax, color = 'darkorange')
#metrics_dataframe.plot(x='epoch', y='loss', ax=ax, color = 'red')
plt.legend(ncol=1, loc='upper right');
ax.yaxis.grid(True) # Hide the horizontal gridlines
ax.xaxis.grid(False)
ax.margins()
ax.set_ylim(bottom=0)
sns.despine()
#plt.show()
plt.savefig('./graphics.pdf', format='pdf', bbox_inches='tight')