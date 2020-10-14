import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

# 找最适合的类别数

def get_best_n(data):
    score = []
    for i in [2, 3, 4]:
        cluster = KMeans(n_clusters=i, random_state=1).fit(data)
        y_pred = cluster.labels_
        score.append(silhouette_score(data, y_pred))  # (-1,1) 越接近1越好
    return score.index(max(score)) + 2


def kmeans(n_clusters, data):
    color = ["red", "pink", "orange"]
    cluster = KMeans(n_clusters=n_clusters, random_state=1).fit(data)
    labels = cluster.labels_
    # fig, ax1 = plt.subplots(1)
    # for i in range(2):
    #     size = data[cluster.predict(data) == i].shape[0]
    #     ax1.scatter(data[cluster.predict(data) == i], np.zeros(size).reshape(-1, 1), marker='o', s=8, c=color[i])
    # plt.show()
    return labels


