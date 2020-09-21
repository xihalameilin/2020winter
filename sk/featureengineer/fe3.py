import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
data = pd.read_csv(r"D:\kaggle\taitan\mytrain2.csv", index_col=0)
#print(data.head())

#print(data.info())
#填补年龄
Age = data.loc[:, "Age"].values.reshape(-1,1) #sklearn当中特征矩阵必须是二维
#imp_mean = SimpleImputer() #实例化，默认均值填补
imp_median = SimpleImputer(strategy="median") #用中位数填补
# imp_0 = SimpleImputer(strategy="constant", fill_value=0) #用0填补
#imp_mean = imp_mean.fit_transform(Age) #fit_transform一步完成调取结果
# imp_median = imp_median.fit_transform(Age)
# imp_0 = imp_0.fit_transform(Age)
# imp_mean[:20]
# imp_median[:20]
# imp_0[:20]
#在这里我们使用中位数填补Age
data.loc[:, "Age"] = imp_median
# data.info()
#使用众数填补Embarked
Embarked = data.loc[:, "Embarked"].values.reshape(-1,1)

imp_mode = SimpleImputer(strategy="most_frequent")
data.loc[:, "Embarked"] = imp_mode.fit_transform(Embarked)
# print(data.info())



# pandas 和 numpy更方便
# import pandas as pd
# data = pd.read_csv(r"C:\work\learnbetter\micro-class\week 3
# Preprocessing\Narrativedata.csv",index_col=0)
# data.head()
# data.loc[:,"Age"] = data.loc[:,"Age"].fillna(data.loc[:,"Age"].median())
# #.fillna 在DataFrame里面直接进行填补
# data.dropna(axis=0,inplace=True)
# #.dropna(axis=0)删除所有有缺失值的行，.dropna(axis=1)删除所有有缺失值的列
# #参数inplace，为True表示在原数据集上进行修改，为False表示生成一个复制对象，不修改原数据，默认False

y = data.iloc[:, -1] #要输入的是标签，不是特征矩阵，所以允许一维
le = LabelEncoder() #实例化
le = le.fit(y) #导入数据
label = le.transform(y)


print(le.classes_) #属性.classes_查看标签中究竟有多少类别
#print(label) #查看获取的结果label
le.fit_transform(y) #也可以直接fit_transform一步到位
le.inverse_transform(label) #使用inverse_transform可以逆转

# data.iloc[:,-1] = label #让标签等于我们运行出来的结果
# data.head()
# #如果不需要教学展示的话我会这么写：
# from sklearn.preprocessing import LabelEncoder
# data.iloc[:,-1] = LabelEncoder().fit_transform(data.iloc[:,-1])






from sklearn.preprocessing import OrdinalEncoder
#接口categories_对应LabelEncoder的接口classes_，一模一样的功能
data_ = data.copy()
#print(data_.iloc[:, 1:-1])
print(OrdinalEncoder().fit(data_.iloc[:,1:-1]).categories_)
data_.iloc[:,1:-1] = OrdinalEncoder().fit_transform(data_.iloc[:,1:-1])
#print(data_.head())


'''
不同的舱门之间不存在数学关系 此时使用one-hot编码
'''


from sklearn.preprocessing import OneHotEncoder
X = data.iloc[:,1:-1]
enc = OneHotEncoder(categories='auto').fit(X)
result = enc.transform(X).toarray() #性别与舱门分为2+3=5个类别
#print(result)
#依然可以直接一步到位，但为了给大家展示模型属性，所以还是写成了三步
OneHotEncoder(categories='auto').fit_transform(X).toarray()
#依然可以还原
#pd.DataFrame(enc.inverse_transform(result))
#print(enc.get_feature_names())
#result
#result.shape
#axis=1,表示跨行进行合并，也就是将量表左右相连，如果是axis=0，就是将量表上下相连
newdata = pd.concat([data,pd.DataFrame(result)],axis=1)
#print(newdata.head())
newdata.drop(["Sex","Embarked"],axis=1,inplace=True)
newdata.columns =["Age","Survived","Female","Male","Embarked_C","Embarked_Q","Embarked_S"]
print(newdata)

data_2 = data.copy()
from sklearn.preprocessing import Binarizer
X = data_2.iloc[:,0].values.reshape(-1,1) #类为特征专用，所以不能使用一维数组
transformer = Binarizer(threshold=30).fit_transform(X)
print(transformer)