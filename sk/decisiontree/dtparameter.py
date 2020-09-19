import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split


'''
超参数的学习曲线
'''

test = []
wine = load_wine()
Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)

for i in range(10):
    clf = tree.DecisionTreeClassifier(max_depth=i+1
                                      , criterion="entropy"
                                      , random_state=30)
    clf.fit(Xtrain, Ytrain)
    score = clf.score(Xtest, Ytest)
    test.append(score)

plt.plot(range(1, 11), test, color='red', label = "max_depth")
plt.legend()
plt.show()