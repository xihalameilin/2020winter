# -*- coding: utf-8-*-
import jieba
from gensim.models import word2vec


#  去掉中英文状态下的逗号、句号
def clearSen(comment):
    comment = ' '.join('%s' %id for id in comment).replace('，', '').replace('。', '').replace('？', '').replace('！', '').replace('“', '')\
        .replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '').replace('—', '')\
        .replace('《', '').replace('》', '').replace('、', '').replace('‘', '').replace('’', '')  # 去掉标点符号
    return comment


# 用jieba进行分词
comment = open('./射雕英雄传.txt', 'r', encoding='UTF-8').read()
comment = clearSen(comment)
# jiebaTest.load_userdict('./user_dict/userdict_food.txt')
comment = ' '.join(jieba.cut(comment.replace(" ","")))
print(comment[0:100])


# 分完词后保存到新的txt中
fo = open("./afterSeg.txt", "wb")
fo.write(comment.encode('utf-8'))
print("finished!")
fo.close()

# 用 word2vec 进行训练
sentences = word2vec.Text8Corpus(u'./afterSeg.txt')
# 第一个参数是训练语料，第二个参数是小于该数的单词会被剔除，默认值为5, 第三个参数是神经网络的隐藏层单元数，默认为100
model = word2vec.Word2Vec(sentences, min_count=3, size=50, window=5, workers=4)
# ------------------------------------------------------------------------
# Word2vec有很多可以影响训练速度和质量的参数：
# （1） sg=1是skip-gram算法，对低频词敏感，默认sg=0为CBOW算法，所以此处设置为1。
# （2） min_count是对词进行过滤，频率小于min-count的单词则会被忽视，默认值为5。
# （3） size是输出词向量的维数，即神经网络的隐藏层的单元数。值太小会导致词映射因为冲突而影响结果，值太大则会耗内存并使算法计算变慢，大的size需要更多的训练数据, 但是效果会更好，在本文中设置的size值为300维度。
# （4） window是句子中当前词与目标词之间的最大距离，即为窗口。本文设置窗口移动的大小为5。
# （5） negative和sample可根据训练结果进行微调，sample表示更高频率的词被随机下采样到所设置的阈值，默认值为1e-3。
# （6） hs=1表示层级softmax将会被使用，默认hs=0且negative不为0，则负采样将会被选择使用。
# （7） 最后一个主要的参数控制训练的并行:worker参数只有在安装了Cython后才有效，由于本文没有安装Cython的, 使用的单核。
# ------------------------------------------------------------------------

# 保存模型
model.save("word2vec.model")
model.wv.save_word2vec_format("word2vec.model.bin", binary=True)



# 测试
y2 = model.similarity(u"郭靖", u"黄蓉")  # 计算两个词之间的余弦距离
print(u"郭靖", u"黄蓉", 'similarity:', y2)

for i in model.most_similar(u"黄蓉"):  # 计算余弦距离最接近“黄蓉”的10个词
    print(i[0], i[1])

for i in model.most_similar(u"郭靖"):  # 计算余弦距离最接近“郭靖”的10个词
    print(i[0], i[1])
# 训练词向量时传入的两个参数也对训练效果有很大影响，需要根据语料来决定参数的选择，好的词向量对NLP的分类、聚类、相似度判别等任务有重要意义