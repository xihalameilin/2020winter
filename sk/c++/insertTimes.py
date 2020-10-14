import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
from sklearn.preprocessing import Normalizer


data = pd.read_csv(r"csv/insertTime.csv", index_col=0)
data = data['totalTime']
data = np.array(data).reshape(-1, 1)

#找最适合的类别数
score = []
for i in [2, 3, 4, 5]:
    cluster = KMeans(n_clusters=i, random_state=1).fit(data)
    y_pred = cluster.labels_
    score.append(silhouette_score(data, y_pred)) # (-1,1) 越接近1越好

preNclusters = max(score)

X = data
color = ["red", "pink", "orange", "gray", "black"]
cluster = KMeans(n_clusters=preNclusters, random_state=1).fit(X)
y_pred = cluster.labels_
centroid = cluster.cluster_centers_
print(centroid)
fig, ax1 = plt.subplots(1)
for i in range(preNclusters):
    size = X[cluster.predict(X) == i].shape[0]
    ax1.scatter(X[cluster.predict(X) == i], np.zeros(size).reshape(-1, 1), marker='o', s=8, c=color[i])
plt.show()
