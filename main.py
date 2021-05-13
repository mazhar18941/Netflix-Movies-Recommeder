import streamlit as st
import pandas as pd
import movierecommender

st.title('Netflix Movies Recommender')
#st.image('download.jpeg',width=500)
movie = st.text_input('Enter Movie Name','')
if movie:
    movies_r = movierecommender.recommender(movie)

    df = pd.DataFrame(
        movies_r, columns=['Recommended Movie', 'Year of Release', 'Average Rating', 'Probability']
    )

    st.dataframe(df)
#print(movie)
