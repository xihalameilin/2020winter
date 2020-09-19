from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import  GridSearchCV
import pandas as pd
import numpy as np

'''
基于乳腺癌数据集的调参 500+数据  30特征
调整max_depth
'''
data = load_breast_cancer()
param_grid = {'max_depth': np.arange(1, 20, 1)}
rfc = RandomForestClassifier(n_estimators=39,
                             random_state=90)
GS = GridSearchCV(rfc, param_grid, cv=10)
GS.fit(data.data, data.target)

print(GS.best_params_)
print(GS.best_score_)

'''
在这里可以看到在限制了max_depth后模型的准确度下降了，而限制max_depth，
是让模型变得简单了，把模型往左推，即整体的泛化误差上升了，这说明模型
位于图像的左边
此时我们需要增加模型复杂度，需要max_depth大，min_samples_leaf与
min_samples_split小，从而得出结论我们几乎没有参数可以调整了，
除了max_feature,因为后两者是剪枝参数，是在降低模型的复杂度，
此时可以预言已经接近模型的上限
'''



