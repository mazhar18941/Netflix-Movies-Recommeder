import pandas as pd
import string
import gensim
from gensim.models import Word2Vec
import pickle

# loading model
model=gensim.models.KeyedVectors.load_word2vec_format('movie2vec_50.model')

# loading title2movieId dictionary
with open("movie_title.pkl", "rb") as fp:
  title2data = pickle.load(fp)

def preprocessing(title_dict):   # take dict as input and converts it into df and preprocess df
  df = pd.DataFrame.from_dict(title_dict, orient='index', columns=['movie_id', 'year', 'rating']).reset_index().rename(columns={'index': 'title'})
  df['title'] = df['title'].str.lower()
  df['year'] = df['year'].astype(str).str.replace('\.0', '').astype(int)
  df['rating'] = df['rating'].astype(float).round(decimals=2)
  return df

df = preprocessing(title2data)


def getMovieID(movie_name):
  movie_name = movie_name.lower()
  movie_id = df.set_index('title').at[movie_name, 'movie_id']
  return movie_id

def getData(movie_id):
  title = df.set_index('movie_id').loc[movie_id, :]
  title['title'] = string.capwords(title['title'])
  title = title.values.tolist()
  return title

def recommender(movie_name) -> list:
  topn = 10
  movie_id = getMovieID(movie_name)
  recommendation = model.similar_by_word(movie_id, topn=10)
  t_y_r = []
  out = []

  for i in range(topn):

    t_y_r = getData(recommendation[i][0])
    t_y_r.append(recommendation[i][1])    # appending probability
    out.append(t_y_r)
  return out                              # [title, year, rating, prob]


