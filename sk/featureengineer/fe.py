from sklearn.preprocessing import MinMaxScaler
import pandas as pd
data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
print(pd.DataFrame(data))


#数据无量钢化
#实现归一化
scaler = MinMaxScaler() #实例化
scaler = scaler.fit(data) #fit，在这里本质是生成min(x)和max(x)
result = scaler.transform(data) #通过接口导出结果
print(result)  #此处按照列归一化


# result_ = scaler.fit_transform(data) #  上面三行代码可以由这一步直接完成 训练和导出结果一步达成



# scaler.inverse_transform(result) # 转回去 将归一化后的结果逆转


# #使用MinMaxScaler的参数feature_range实现将数据归一化到[0,1]以外的范围中
# data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
# scaler = MinMaxScaler(feature_range=[5,10]) #依然实例化
# result = scaler.fit_transform(data) #fit_transform一步导出结果
# print(result)



# #当X中的特征数量非常多的时候，fit会报错并表示，数据量太大了我计算不了
# #此时使用partial_fit作为训练接口
# #scaler = scaler.partial_fit(data)