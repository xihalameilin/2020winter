from sklearn.cluster import KMeans
import numpy
import collections
import pandas
from sklearn import metrics


def k_means(pp1, clus):
    pv = list(pp1)
    if len(set(pv)) > clus:
        gf = numpy.array([pv]).T
        estimator = KMeans(n_clusters=clus)  # 构造聚类器

        estimator.fit(gf)  # 聚类
        label_pred = estimator.labels_  # 获取聚类标签

        # print(label_pred)
        aa = collections.Counter(label_pred)

        print('aa=', aa)
        v = pandas.Series(aa)
        gg = list(v)
        index_max = gg.index(max(gg))

        print('index_max=', index_max)

        centroids = estimator.cluster_centers_  # 获取聚类中心

        print('centroids=', centroids)
        # inertia = estimator.inertia_ # 获取聚类准则的总和
        center = centroids[index_max][0]
        return ((center))
    else:
        return (pp1.mean())


def k_means_label(a):
    def km_index(k):
        pv = list(a)

        gf = numpy.array([pv]).T

        # from sklearn.cluster import KMeans
        y_pred = KMeans(n_clusters=k, random_state=9).fit_predict(gf)

        index = metrics.silhouette_score(gf, y_pred, metric='euclidean')

        print('index', index)

        return index

    cs = list(range(2, 6))

    df = list(map(km_index, cs))

    df1 = pandas.Series(df, index=cs)
    df2 = df1.sort_values(ascending=False)

    df3 = list(df2.index)[0]

    return df3


a = numpy.random.randint(0, 1000, 10)

cc = k_means_label(a)

b = k_means(a, cc)

print('b=', b)