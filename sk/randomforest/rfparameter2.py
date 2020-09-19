from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import  GridSearchCV
import pandas as pd
import numpy as np

'''
基于乳腺癌数据集的调参 500+数据  30特征
确定n_estimators在41左右
'''

data = load_breast_cancer()

score_1 = []
for i in range(35, 45):
    rfc = RandomForestClassifier(n_estimators=i,
                                 n_jobs=-1,
                                 random_state=90)
    score = cross_val_score(rfc, data.data, data.target, cv=10).mean()
    score_1.append(score)
print(max(score_1), ([*range(35, 45)][score_1.index(max(score_1))]))
plt.figure(figsize=[20, 5])
plt.plot(range(35, 45), score_1)
plt.show()




