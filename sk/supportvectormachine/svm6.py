from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from time import time
import datetime
import pandas as pd
'''
乳腺癌数据集 500+数据 30特征 二分类
'''

data = load_breast_cancer()
X = data.data
y = data.target
# plt.scatter(X[:, 0], X[:, 1], c=y)
# plt.show()

data = pd.DataFrame(X)
data.describe([0.01,0.05,0.1,0.25,0.5,0.75,0.9,0.99]).T
#此数据集量纲不统一 偏态问题

'''
degree参数用来限制poly多项式核函数
'''

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.3, random_state=420)
Kernel = ["linear", "poly", "rbf", "sigmoid"]
for kernel in Kernel:
    time0 = datetime.datetime.now()
    clf = SVC(kernel=kernel, gamma="auto"
              #, degree=1
              , cache_size=5000).fit(Xtrain, Ytrain)
    print("The accuracy under kernel %s is %f" % (kernel, clf.score(Xtest, Ytest)))
    print((datetime.datetime.now()-time0).seconds)