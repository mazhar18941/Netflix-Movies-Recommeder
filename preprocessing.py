import pandas as pd
import time
import pickle

# unzipped files from dataset
files = ['combined_data_1.txt',
         'combined_data_2.txt',
         'combined_data_3.txt',
         'combined_data_4.txt']

s = time.time()
data = open('data.csv', 'w')

for file in files:
  print('reading {}...'.format(file))
    
  with open(file) as f:

      for line in f:

        line = line.strip()

        if line.endswith(':'):
          movie_id = line.replace(':','')

        else:
          line_l = line.split(',')
          user_id = line_l[0]
          rating = line_l[1]
          data.write(movie_id+','+user_id+','+rating)
          data.write('\n')
  print('Done...')

data.close()

t = time.time()
print('Writing *.txt to Data.csv Time Taken: ',t-s)

# in order to save memory variables name 'data' is re-used
start = time.time()

data = pd.read_csv('data.csv',
                   sep=',',
                   names=['movie_id','user_id','rating'])

print('Loading Data.csv Time Taken: ',time.time()-start)

print('size of Data.csv',len(data))

rating_avg = data.groupby('movie_id')['rating'].mean()

# will be used later
def getTitleDict(csv_path, rating_avg):   # return a dict
  title = pd.read_csv(csv_path,
                    usecols=[0,1,2],
                    encoding='ISO-8859-1',
                    names = ['movie_id', 'year', 'title'])
  
  title['avg_rating'] = rating_avg
  title.dropna(inplace=True)
  title_l = title.astype(str).set_index('title').values.tolist()
  title_dict = {k:v for k,v in zip(title['title'].values, title_l)}

  return title_dict

# movie_title.csv in dataset
title_dict = getTitleDict('movie_titles.csv', rating_avg)  # dictionary

with open("movie_title.pkl", "wb") as fp:
   pickle.dump(title_dict, fp)

print('movie_titles.csv Saved...')

len(title_dict)

# pandas to dictionary
import time
s = time.time()
data = data.groupby('user_id')['movie_id'].apply(list).to_dict()
print('Converting to Dictionary Time Taken: ',time.time()-s)

len(data)  # equal to no. of users...nice

''' creating a list of lists where each element represents user's watch history
    [[mov1,mov2,mov3,...,movN],[mov3,mov6,...movK]...[mov111,mov984,...movY]]'''

data = list(data.values())   # user2movie # creating a list of lists

# mount drive before running this cell if u want to permanently save file in colab
s = time.time()

#Pickling list of sentences to location
with open("watch_history.pkl", "wb") as fp:
   pickle.dump(data, fp)

print('Saving watch_history Time Taken: ',time.time()-s)

"""we could not convert list elements to str because str require more space than int. So, we have to save file to location and then load it in after restarting runtime.
NOTE: Model accepts str so we have to convert movie_id to str after file is loaded.
"""

# test that everthing saved safely.
'''with open("/content/drive/MyDrive/ColabData/NetflixData/watch_history.pkl", "rb") as fp:
  data = pickle.load(fp)

print(len(data))'''

