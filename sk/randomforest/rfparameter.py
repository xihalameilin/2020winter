from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import  GridSearchCV
import pandas as pd
import numpy as np

'''
基于乳腺癌数据集的调参 500+数据  30特征
'''

data = load_breast_cancer()

score_1 = []
for i in range(0, 200, 10):
    rfc = RandomForestClassifier(n_estimators=i+1,
                                 n_jobs=-1,
                                 random_state=90)
    score = cross_val_score(rfc, data.data, data.target, cv=10).mean()
    score_1.append(score)

print(max(score_1), (score_1.index(max(score_1))*10)+1)
plt.figure(figsize=[20, 5])
plt.plot(range(1, 201, 10), score_1)
plt.show()




