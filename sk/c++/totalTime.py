import pandas as pd
import util
import numpy as np

data = pd.read_csv(r"C:\Users\hp\PycharmProjects\2020winter\sk\c++\csv\totalTime.csv")
userIds = np.array(data['userId'])
data = data['totalTime']
data = np.array(data).reshape(-1, 1)




n_cluster = util.get_best_n(data)
print(n_cluster)
print(userIds)
print(util.kmeans(n_cluster, data))





