import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, SGDRegressor, LogisticRegression



def logistic():
    path = 'breast-cancer-wisconsin.csv'#更改此处地址
    column = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
              'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli',
              'Mitoses', 'Class']

    data = pd.read_csv(path, names=column)
    ##缺失值进行数据处理
    data = data.replace(['?'], np.nan)
    ##print(data)
    data = data.dropna()  # 将空缺值删除
    # 进行数据的分割
    x_train, x_test, y_train, y_test = train_test_split(data[column[1:10]], data[column[10]], test_size=0.25)

    std = StandardScaler()# 数据标准化
    ##print('be4',x_train,x_test)
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)
    ##print('After',x_train, x_test)
    # 逻辑回归开始预测
    lg = LogisticRegression(C=1.0)
    lg.fit(x_train, y_train)
    ##print(lg.coef_)  # 十个特征值的参数
    y_predict = lg.predict(x_test)


    print(lg.predict(x_test[0:4]))

    print("准确率：", lg.score(x_test, y_test))
    print("召回率：", classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"]))

    return None


if __name__ == "__main__":
    logistic()