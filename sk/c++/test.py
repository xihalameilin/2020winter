import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv(r"csv/totalTime_9.csv", index_col=0)
data = data['totalTime']
data = np.array(data).reshape(-1, 1)

score = []
score2 = []
fig, ax1 = plt.subplots(1)
for i in [2, 3, 4, 5]:
    cluster = KMeans(n_clusters=i, random_state=1).fit(data)
    y_pred = cluster.labels_
    score.append(silhouette_score(data, y_pred)) # (-1,1) 越接近1越好
    score2.append(cluster.inertia_)
ax1.plot([2, 3, 4, 5], score, 'r--', label='K 与 轮廓系数的关系')
ax1.plot([2, 3, 4, 5], score2, 'r--', label='K 与 SSE的关系')
plt.xlabel('K')
plt.ylabel('轮廓系数')
plt.legend()
# plt.savefig("/")
plt.show()

