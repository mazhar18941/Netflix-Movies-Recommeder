# Netflix-Movies-Recommeder
This is a movie recommendation system trained on Netflix movies dataset(https://www.kaggle.com/netflix-inc/netflix-prize-data). It uses deep learning technique skip-gram word2vec in order to extract word embeddings from movies corpus. Word embedding is a vector which captures context of the word in corpus and very popular in NLP. Then, similarity of these embeddings is computed and given a movie name, top 10 most watched movies alongside given movie are returned and displayed in streamlit App.

There are 4 python files;

preprocessing.py --> outputs a list containing watch history of each user. There are 480189 users and 17770 movies in a dataset.
training.py      --> model is trained on sequences(watch history of users) and produces word embeddings of size (number of movies, 50). 			      Vector size is set to 50.
movierecommeder.py --> cosine similarity is computed. As movie names are encoded with integer numbers, we have to convert them back to movies names.
main.py           --> streamlit app
