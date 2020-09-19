from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
'''
随机森林是集成算法的一种
随机森林参数与决策树类似
特有的参数如下：
1. n_estimators  森林中树木的数量，即基评估器的数量，越大，模型效果往往越好，但不可太大



常用接口：
1. apply
2. fit
3. predict
4. score
5. predict_proba 返回测试样本对应的被分到每个标签的概率


调参：
影响程度： n_estimators > max_depth > min_samples_leaf > min_samples_split > max_features > criterion


'''

wine = load_wine()
Xtrain, Xtest ,Ytrain ,Ytest = train_test_split(wine.data,wine.target,test_size=0.3)



#
# clf.fit(Xtrain, Ytrain)
# rfc.fit(Xtrain, Ytrain)

# score_c = clf.score(Xtest, Ytest)
# score_r = rfc.score(Xtest, Ytest)

rfc_1 = []
clf_1 = []


for i in range(10):
    clf = DecisionTreeClassifier()
    rfc = RandomForestClassifier(n_estimators=25)
    #交叉验证的均值作为一次循环的结果
    rfc_s = cross_val_score(rfc,wine.data,wine.target,cv=10).mean()
    clf_s = cross_val_score(clf,wine.data,wine.target,cv=10).mean()
    rfc_1.append(rfc_s)
    clf_1.append(clf_s)
plt.plot(range(1,11), rfc_1 , label = "random forest")
plt.plot(range(1,11), clf_1 , label = "decision tree")
plt.legend()
plt.show()