from gensim import corpora, models, similarities
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
texts = [['human', 'interface', 'computer'],
 ['survey', 'user', 'computer', 'system', 'response', 'time'],
 ['eps', 'user', 'interface', 'system'],
 ['system', 'human', 'system', 'eps'],
 ['user', 'response', 'time'],
 ['trees'],
 ['graph', 'trees'],
 ['graph', 'minors', 'trees'],
 ['graph', 'minors', 'survey']]

dictionary = corpora.Dictionary(texts)
#dictionary.save('dic.txt')
print(dictionary.token2id)

new_doc = 'Human computer interaction'
# doc2bow 计算不同单词出现的次数 将结果作为稀疏矩阵返回
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec)

corpus = [dictionary.doc2bow(text) for text in texts]
print(corpus)

tfidf = models.TfidfModel(corpus)
print(tfidf[new_vec])

corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
 print(doc)

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
corpus_lsi = lsi[corpus_tfidf]
print('1111111111111111')
for item in corpus_lsi:
 print(item)
print('1111111111111111')

# lsi.print_topics(2)
#for doc in corpus_lsi:
# print(doc)
print('--------------------')
vec_lsi = lsi[new_vec]
print("主题分布"+str(vec_lsi))


index = similarities.MatrixSimilarity(lsi[corpus])
print('222222222222')
for item in index:
 print(item)
print('222222222222')
sims = index[vec_lsi]
print(list(enumerate(sims)))

sims = sorted(enumerate(sims), key=lambda  item : -item[1])
print(sims)