import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
data = pd.read_csv(r"mytrain2.csv", index_col=0)

data_2 = data.copy()
data_2.loc[:, "Age"] = data_2.loc[:, "Age"].fillna(data_2.loc[:, "Age"].median())
from sklearn.preprocessing import Binarizer
X = data_2.iloc[:,0].values.reshape(-1,1) #类为特征专用，所以不能使用一维数组
transformer = Binarizer(threshold=30).fit_transform(X)
print(transformer)
