from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import pandas as pd
import pydotplus
import io

"""
决策树的实现：
算法最重要的问题：1.如何从数据表中找出最佳节点和最佳分支 2.如何让局册数停止生长，防止过拟合

参数：  
1. criterion  可选为entropy/gini 确定不纯度的计算方法，越低越好，同时使用基尼系数，数据维度大噪音大使用基尼系数，维度低没区别
2. random_state  用来设置分支中随机模式的参数，默认为None
3. splitter  可选为best/random 默认best random可能导致树加深，是防止过拟合的一种方式
为了让决策树有更好的泛化性，我们要对决策树进行剪枝，剪枝策略对决策树的英影响巨大，正确的策略是优化算法的核心
一下为sklearn提供的不同剪枝策略：
max_depth  最广泛使用，高纬度低样本量时非常有效，决策树多生长一层对样本的需求就会增加一倍，在实际使用中，建议从3开始
min_sample_leaf 一个节点在分支后的每个子节点都必须包含至少min_sample_leaf个样本，否则分支不发生，一般搭配max_depth使用，一般建议从5开始
min_sample_split  一个节点必须要包含至少min_sample_split个训练样本，这个节点才允许被分支，否则分支不发生
max_features
min_impurity_decrease
通常使用max_depth与(min_sample_leaf/min_sample_split)中一个

图：节点颜色越深越有效
"""



wine = load_wine()
jointData = pd.concat([pd.DataFrame(wine.data), pd.DataFrame(wine.target)], axis=1)
#此处划分数据集是随机的
Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(Xtrain, Ytrain)
score = clf.score(Xtest, Ytest)
print(score)
# dot_data = io.StringIO()
feature_names = ['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']
# tree.export_graphviz(clf,
#                      out_file=dot_data,
#                      feature_names=feature_names,
#                      class_names=["酒1", "酒2", "酒3"],
#                      filled=True,  #显示颜色
#                      rounded=True) #node形状
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# graph.write_svg("Tree.svg")


print(clf.feature_importances_) #每个特征数值越大越重要
print([*zip(feature_names, clf.feature_importances_)])

print(clf.apply(Xtest))  #返回所在叶子节点的索引
print(clf.predict(Xtest)) #返回标签
# graph = graphviz.Source(dot_data)
# graph.render(view=True,format="pdf",filename="decisiontree.pdf")
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf("2.pdf")
