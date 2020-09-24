from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import datetime
import pandas as pd
from sklearn.preprocessing import StandardScaler
'''
乳腺癌数据集 500+数据 30特征 二分类
由于数据的问题 进行标准化(0到1的正态分布)
SVM是在高维度进行计算，所以数据标准化对它的计算非常有帮助
线性核，尤其是多项式核函数在高次项时计算非常缓慢
rbf和多项式核函数都不擅长处理量纲不统一的数据集
幸运的是，这两个缺点都可以由数据无量纲化来解决。因此，SVM执行之前，非常推荐先进行数据的无量纲化！
线性linear无参数可以调整
rbf等还有参数可以调整
'''

data = load_breast_cancer()
X = data.data
y = data.target

data = pd.DataFrame(X)
X = StandardScaler().fit_transform(X)
#此数据集量纲不统一 偏态问题


Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.3, random_state=420)
Kernel = ["linear", "poly", "rbf", "sigmoid"]
for kernel in Kernel:
    time0 = datetime.datetime.now()
    clf = SVC(kernel=kernel
              , gamma="auto"
              , degree=1
              , cache_size=5000).fit(Xtrain, Ytrain)
    print("The accuracy under kernel %s is %f" % (kernel, clf.score(Xtest, Ytest)))
    print((datetime.datetime.now()-time0).seconds)