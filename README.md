# Netflix-Movies-Recommeder
## Demo
![Demo](https://github.com/mazhar18941/Netflix-Movies-Recommeder/blob/7f0a546ea1033a8a0e8cc6406fcdfed027ca19f0/gif_demo.gif)
## Goal
This project recommends movies based on watch history of Netflix users. If you search a movie, system will recommend top 10 movies that are watched by Netflix users alongwith searched movie.

## Introduction
This is a movie recommendation system trained on Netflix movies dataset(https://www.kaggle.com/netflix-inc/netflix-prize-data). It uses deep learning technique skip-gram word2vec in order to extract word embeddings from movies corpus. Word embedding is a vector which captures context of the word in corpus and very popular in NLP. Then, similarity of these embeddings is computed and given a movie name, top 10 most watched movies alongside given movie are returned and displayed in streamlit App.

## About Code
There are 4 python files;

preprocessing.py   --> outputs a list containing watch history of each user. There are 480189 users and 17770 movies in a                              dataset.

training.py        --> model is trained on sequences(watch history of users) and produces word embeddings of size (number of                          movies, 50). Vector size is set to 50.

movierecommeder.py --> cosine similarity is computed. As movie names are encoded with integer numbers, we have to convert them                        back to movies names.

main.py           --> streamlit app

## Usage
Project can be used in two ways;

1) Pre-trained model

You need movierecommeder.py and main.py files. Run main.py and streamlit web app will open where search can be carried out.

2) Customized training

You may tune model hyperparameters yourself in training.py.

Run files in following order;

preprocessing.py

training.py

main.py
