import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
data = pd.read_csv(r"mytrain2.csv", index_col=0)
data.index = data.index-1

data.loc[:, "Age"] = data.loc[:, "Age"].fillna(data.loc[:, "Age"].median())
Embarked = data.loc[:, "Embarked"].values.reshape(-1,1)
imp_mode = SimpleImputer(strategy="most_frequent")
data.loc[:, "Embarked"] = imp_mode.fit_transform(Embarked)

y = data.iloc[:, -1] #要输入的是标签，不是特征矩阵，所以允许一维
# le = LabelEncoder() #实例化
# le = le.fit(y) #导入数据
# label = le.transform(y)


# print(le.classes_) #属性.classes_查看标签中究竟有多少类别
# #print(label) #查看获取的结果label
# le.fit_transform(y) #也可以直接fit_transform一步到位
# le.inverse_transform(label) #使用inverse_transform可以逆转

# data.iloc[:,-1] = label #让标签等于我们运行出来的结果
# data.head()
# #如果不需要教学展示的话我会这么写：
# from sklearn.preprocessing import LabelEncoder
# data.iloc[:,-1] = LabelEncoder().fit_transform(data.iloc[:,-1])

'''
不同的舱门之间不存在数学关系 此时使用one-hot编码
'''
from sklearn.preprocessing import OneHotEncoder
X = data.iloc[:, 1:-1]
result = OneHotEncoder(categories='auto').fit_transform(X).toarray()
#axis=1,表示跨行进行合并，也就是将量表左右相连，如果是axis=0，就是将量表上下相连
newdata = pd.concat([data, pd.DataFrame(result)], axis=1)
newdata.drop(["Sex", "Embarked"], axis=1, inplace=True)
newdata.columns = ["Age", "Survived", "Embarked_C", "Embarked_Q", "Embarked_S", "Female", "Male"]
print(newdata)