from sklearn import svm

X = [[0, 1], [2, 2]]
y = [0, 1]
clf = svm.SVR()
clf.fit(X, y)
print(clf.predict([[1, 2]]))