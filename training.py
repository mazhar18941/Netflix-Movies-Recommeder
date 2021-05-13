import pandas as pd
import gensim
from gensim.models import Word2Vec

import time
import pickle

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# loading watch history of users(dictionary)

with open("watch_history.pkl", "rb") as fp: # list in int format
  sentences = pickle.load(fp)

print('No. of sequences: ',len(sentences) )  # equal to no. of users...nice


''' converting each movie_id dtype to str because model accepts strings '''
start = time.time()

user2movie_s = []
for l in sentences:
  s = [str(x) for x in l]
  user2movie_s.append(s)

sentences = user2movie_s
del user2movie_s

print('Time Taken: ',time.time()-start)

#len(sentences)  # equal to no. of users...nice

# training word2vec model
model = Word2Vec(window = 5, sg = 1, hs = 0,
                 negative = 10,
                 seed = 14, size=50)

model.build_vocab(sentences, progress_per=200)

model.train(sentences, total_examples = model.corpus_count, 
            epochs=5, report_delay=1)

model.wv.save_word2vec_format('movie2vec_50.model')



