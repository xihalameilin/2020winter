import logging
from gensim.models import word2vec

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.LineSentence('./in_the_name_of_people_segment.txt')

model = word2vec.Word2Vec(sentences, hs=1, min_count=1, window=3, size=100)

model.save("word2vec.model")
model.wv.save_word2vec_format("word2vec.model.bin", binary=True)


