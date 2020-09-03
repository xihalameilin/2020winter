texts = [['human', 'interface', 'computer'],
['survey', 'user', 'computer', 'system', 'response', 'time'],
['eps', 'user', 'interface', 'system'],
['system', 'human', 'system', 'eps'],
['user', 'response', 'time'],
['trees'],
['graph', 'trees'],
['graph', 'minors', 'trees'],
['graph', 'minors', 'survey']]


from gensim import corpora, models
from gensim.similarities import Similarity

dictionary = corpora.Dictionary(texts)
# 转化为稀疏矩阵corpus（语料库）
corpus = [dictionary.doc2bow(text) for text in texts]

tfidf = models.TfidfModel(corpus)
corpus_tdidf = [tfidf[doc] for doc in corpus]
for item in corpus_tdidf:
    print(item)
print('------------------------')
# 使用tfidf代入计算
lsi_model = models.LsiModel(corpus_tdidf, id2word=dictionary, num_topics=2)
# 主题向量
documents = [lsi_model[doc] for doc in corpus]
for item in documents:
    print(item)


similarity = Similarity('Similarity-Lsi-index', documents, num_features=400)


test_cut_raw_1 = ['human', 'trees'],
test_corpus_3 = dictionary.doc2bow(test_cut_raw_1)
print(test_corpus_3)
test_corpus_tfidf_3 = tfidf[test_corpus_3]
test_corpus_lsi_3 = documents[test_corpus_tfidf_3]
print(similarity[test_corpus_lsi_3])


#query_text = [['human', 'trees']]
#query_dic = corpora.Dictionary(query_text)
#query = [query_dic.doc2idx(text) for text in query_text]
#query_vec = lsi_model[query]
#print(query)


