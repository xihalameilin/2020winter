#数据标准化 均值为0 方差为1 标准正态分布
from sklearn.preprocessing import StandardScaler
data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
scaler = StandardScaler() #实例化
scaler.fit(data) #fit，本质是生成均值和方差
print(scaler.mean_) #查看均值的属性mean_
print(scaler.var_) #查看方差的属性var_
x_std = scaler.transform(data) #通过接口导出结果
print(x_std.mean()) #导出的结果是一个数组，用mean()查看均值
print(x_std.std()) #用std()查看方差
scaler.fit_transform(data) #使用fit_transform(data)一步达成结果
scaler.inverse_transform(x_std) #使用inverse_transform逆转标准化