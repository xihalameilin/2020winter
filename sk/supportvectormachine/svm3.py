from sklearn.datasets import make_circles
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

'''
非线性: 一眼看过去不能找到决策边界  增加一个维度r  将数据投影到高维空间成为核变换
'''

# def plot_svc_decision_function(model, ax=None):
#     if ax is None:
#         ax = plt.gca()
#     xlim = ax.get_xlim()
#     ylim = ax.get_ylim()
#
#     x = np.linspace(xlim[0], xlim[1], 30)
#     y = np.linspace(ylim[0], ylim[1], 30)
#     Y, X = np.meshgrid(y, x)
#     xy = np.vstack([X.ravel(), Y.ravel()]).T
#     Z = model.decision_function(xy).reshape(X.shape)
#
#     ax.contour(X, Y, Z, colors="k", levels=[-1, 0, 1], alpha=0.5, linestyles=["--", "-", "--"])
#     ax.set_xlim(xlim)
#     ax.set_ylim(ylim)


X, y = make_circles(100, factor=0.1, noise=.1)
clf = SVC(kernel="linear").fit(X, y)
# plot_svc_decision_function(clf)

#定义一个由x计算出来的新维度r
r = np.exp(-(X**2).sum(1))
rlim = np.linspace(min(r), max(r), 100)
#定义一个绘制三维图像的函数
#elev表示上下旋转的角度
#azim表示平行旋转的角度
def plot_3D(elev=30, azim=30, X=X, y=y):
    ax = plt.subplot(projection="3d")
    ax.scatter3D(X[:, 0], X[:, 1], r, c=y, s=50, cmap='rainbow')
    ax.view_init(elev=elev, azim=azim)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("r")
    plt.show()
plot_3D()