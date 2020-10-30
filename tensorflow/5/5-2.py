import datetime
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models


# 打印日志
def printlog(info):
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\n" + "==========" * 8 + "%s" % nowtime)
    print(info + '...\n\n')


dftrain_raw = pd.read_csv("train.csv")
dftest_raw = pd.read_csv("test.csv")

dfraw = pd.concat([dftrain_raw, dftest_raw])

print(dfraw.columns)
print(dfraw.dtypes)


def prepare_dfdata(dfraw):
    dfdata = dfraw.copy()
    dfdata.columns = [x.lower() for x in dfdata.columns]
    dfdata = dfdata.rename(columns={'survived': 'label'})
    dfdata = dfdata.drop(['passengerid', 'name'], axis=1)
    for col, dtype in dict(dfdata.dtypes).items():
        if dfdata[col].hasnans:
            dfdata[col + '_nan'] = pd.isna(dfdata[col]).astype('int32')
            if dtype not in [np.object, np.str, np.unicode]:
                dfdata[col].fillna(dfdata[col].mean(), inplace=True)
            else:
                dfdata[col].fillna('', inplace=True)
    return dfdata


dfdata = prepare_dfdata(dfraw)
dftrain = dfdata.iloc[0:len(dftrain_raw), :]
dftest = dfdata.iloc[len(dftrain_raw):, :]


def df_to_dataset(df, shuffle=True, batch_size=32):
    dfdata = df.copy()
    if 'label' not in dfdata.columns:
        ds = tf.data.Dataset.from_tensor_slices(dfdata.to_dict(orient='list'))
    else:
        labels = dfdata.pop('label')
        ds = tf.data.Dataset.from_tensor_slices(dfdata.to_dict(orient='list'))
    if shuffle:
        ds = ds.shuffle(buffer_size=len(dfdata))
    ds = ds.batch(batch_size)
    return ds


ds_train = df_to_dataset(dftrain)
ds_test = df_to_dataset(dftest)

printlog("step2: make feature columns...")

feature_columns = []

# 数值列
for col in ['age', 'fare', 'parch', 'sibsp'] + [
    c for c in dfdata.columns if c.endswith('_nan')]:
    feature_columns.append(tf.feature_column.numeric_column(col))

# 分桶列
age = tf.feature_column.numeric_column('age')
age_buckets = tf.feature_column.bucketized_column(age,
                                                  boundaries=[18, 25, 30, 35, 40, 45, 50, 55, 60, 65])
feature_columns.append(age_buckets)

# 类别列
# 注意：所有的Catogorical Column类型最终都要通过indicator_column转换成Dense Column类型才能传入模型！！
sex = tf.feature_column.indicator_column(
    tf.feature_column.categorical_column_with_vocabulary_list(
        key='sex', vocabulary_list=["male", "female"]))
feature_columns.append(sex)

pclass = tf.feature_column.indicator_column(
    tf.feature_column.categorical_column_with_vocabulary_list(
        key='pclass', vocabulary_list=[1, 2, 3]))
feature_columns.append(pclass)

ticket = tf.feature_column.indicator_column(
    tf.feature_column.categorical_column_with_hash_bucket('ticket', 3))
feature_columns.append(ticket)

embarked = tf.feature_column.indicator_column(
    tf.feature_column.categorical_column_with_vocabulary_list(
        key='embarked', vocabulary_list=['S', 'C', 'B']))
feature_columns.append(embarked)

# 嵌入列
cabin = tf.feature_column.embedding_column(
    tf.feature_column.categorical_column_with_hash_bucket('cabin', 32), 2)
feature_columns.append(cabin)

# 交叉列
pclass_cate = tf.feature_column.categorical_column_with_vocabulary_list(
    key='pclass', vocabulary_list=[1, 2, 3])

crossed_feature = tf.feature_column.indicator_column(
    tf.feature_column.crossed_column([age_buckets, pclass_cate], hash_bucket_size=15))

feature_columns.append(crossed_feature)

print(feature_columns)
