from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score,silhouette_samples
import numpy as np




'''
聚类前的可视化，肉眼看看
'''
X = np.random.rand(100)*100
X = X.reshape(-1, 1)
# #建立子图 一个
# fig, ax1 = plt.subplots(1)
# '''
# marker: 点的形状
# s: 点的大小
# '''
# ax1.scatter(X[:, 0], X[:, 1], marker='o', s=8)
# plt.show()


color = ["red", "pink", "orange", "gray"]
cluster = KMeans(n_clusters=3, random_state=1).fit(X)
y_pred = cluster.labels_
fig, ax1 = plt.subplots(1)
for i in range(3):
    size = X[cluster.predict(X) == i].shape[0]
    ax1.scatter(X[cluster.predict(X) == i], np.zeros(size).reshape(-1, 1), marker='o', s=8, c=color[i])
plt.show()


# score = []
# fig, ax1 = plt.subplots(1)
# for i in [2, 3, 4, 5]:
#     cluster = KMeans(n_clusters=i, random_state=1).fit(X)
#     y_pred = cluster.labels_
#     score.append(silhouette_score(X, y_pred)) # (-1,1) 越接近1越好
# ax1.plot([2, 3, 4, 4], score, 'r--', label='K 与 轮廓系数的关系')
# plt.show()
