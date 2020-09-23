from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score,silhouette_samples




'''
聚类前的可视化，肉眼看看
'''
X, y = make_blobs(n_samples=500, n_features=2, centers=4, random_state=1)
# #建立子图 一个
# fig, ax1 = plt.subplots(1)
# '''
# marker: 点的形状
# s: 点的大小
# '''
# ax1.scatter(X[:, 0], X[:, 1], marker='o', s=8)
# plt.show()


# color = ["red", "pink", "orange", "gray"]
# fig, ax1 = plt.subplots(1)
# for i in range(4):
#     ax1.scatter(X[y == i, 0], X[y == i, 1], marker='o', s=8, c=color[i])
# plt.show()

n_clusters = 3
cluster = KMeans(n_clusters=n_clusters, random_state=0).fit(X)
y_pred = cluster.labels_  #返回一堆的0 1 2
#print(y_pred)
# pre = cluster.fit_predict(X)
# pre == y_pred 全部是true 不需要调用这个接口
centroid = cluster.cluster_centers_
#print(centroid)  #三个质心坐标
#print(centroid.shape) #(3,2)
inertia = cluster.inertia_
print(inertia) #总距离平方和

color = ["red", "pink", "orange", "gray"]
fig, ax1 = plt.subplots(1)
for i in range(n_clusters):
    ax1.scatter(X[y_pred == i, 0], X[y_pred == i, 1], marker='o', s=8,c =color[i])
#画出质心
ax1.scatter(centroid[:, 0], centroid[:, 1], marker="x", s=15, c="black")
plt.show()


silhouette_score(X, y_pred) # 分3个簇轮廓系数  0.58 (-1,1) 越接近1越好


#簇的个数会影响inertia
# n_clusters = 4
# cluster_ = KMeans(n_clusters=n_clusters, random_state=0).fit(X)
# inertia_ = cluster_.inertia_
# inertia_