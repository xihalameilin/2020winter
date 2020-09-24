from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV


'''
poly调整参数 gamma coef0
'''

data = load_breast_cancer()
X = data.data
y = data.target
data = pd.DataFrame(X)
X = StandardScaler().fit_transform(X)


gamma_range = np.logspace(-10, 1, 20)
coef0_range = np.linspace(0, 5, 10)
param_grid = dict(gamma=gamma_range, coef0=coef0_range)
cv = StratifiedShuffleSplit(n_splits=5, test_size=0.3, random_state=420)
grid = GridSearchCV(SVC(kernel="poly", degree=1, cache_size=5000), param_grid=param_grid, cv=cv)
grid.fit(X, y)
print("The best parameters are %s with a score of %0.5f" % (grid.best_params_, grid.best_score_))
