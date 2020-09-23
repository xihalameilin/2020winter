from sklearn.datasets import make_blobs
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

X, y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.6)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="rainbow") #颜色y 尺寸50
# #横坐标纵坐标显示为空
# plt.xticks([])
# plt.yticks([])
# plt.show()

ax = plt.gca() #获取当前的子图，如果不存在，则创建新的子图
#获取平面上两条坐标轴的最大值和最小值
xlim = ax.get_xlim()
ylim = ax.get_ylim() #默认创建(0.0, 1.0)范围内的横纵坐标


#要画决策边界，必须要有网格
axisx = np.linspace(xlim[0], xlim[1], 30)
axisy = np.linspace(ylim[0], ylim[1], 30)

axisy, axisx = np.meshgrid(axisy, axisx)



#将特征向量转换为特征矩阵的函数
#核心是将两个特征向量广播，以便获取y.shape * x.shape这么多个坐标点的横坐标和纵坐标
#ravel 二维拉成一维
xy = np.vstack([axisx.ravel(), axisy.ravel()]).T
plt.scatter(xy[:, 0], xy[:, 1], s=1, cmap="rainbow")
# plt.show()


#建模，通过fit计算出对应的决策边界
clf = SVC(kernel="linear").fit(X, y)
Z = clf.decision_function(xy).reshape(axisx.shape)
#重要接口decision_function，返回每个输入的样本所对应的到决策边界的距离
#然后再将这个距离转换为axisx的结构
#画决策边界和平行于决策边界的超平面
#画三条等高线 分别为Z=-1，0，1
ax.contour(axisx, axisy, Z, colors="k", levels=[-1, 0, 1], alpha=0.5, linestyles=["--", "-", "--"])
ax.set_xlim(xlim)
ax.set_ylim(ylim)
plt.show()