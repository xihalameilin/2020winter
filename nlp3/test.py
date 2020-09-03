import gensim

result_path = 'word2vec.model'
model = gensim.models.Word2Vec.load(result_path)


#找出相似的词
req_count = 5
for key in model.wv.similar_by_word('沙瑞金'.encode('utf-8').decode('utf-8'), topn=100):
    if len(key[0]) == 3:
        req_count -= 1
        print(key[0], key[1])
        if req_count == 0:
            break;

#词向量相似度
print(model.wv.similarity('沙瑞金'.encode('utf-8').decode('utf-8'), '高育良'.encode('utf-8').decode('utf-8')))
print(model.wv.similarity('李达康'.encode('utf-8').decode('utf-8'), '王大路'.encode('utf-8').decode('utf-8')))
#找不匹配
print(model.wv.doesnt_match(u"沙瑞金 高育良 李达康 刘庆祝".split()))
