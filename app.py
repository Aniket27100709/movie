import streamlit as st
import pandas as pd
import pickle
import requests


def fetch_movie(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=16f23778b5a68f84baa53bf8a1ba80de&language=en-US'.format(movie_id))
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(obj):
    index = movie[movie['title'] == obj].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    l = []
    img = []
    for i in distances[1:7]:
        id = movie.iloc[i[0]].movie_id
        img.append(fetch_movie(id))
        l.append(movie.iloc[i[0]].title)
    return l, img


movies = pickle.load(open('movied.pkl', 'rb'))
movie = pd.DataFrame(movies)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation Application')

options = st.selectbox(
    "Which Movie Would you like to watch?", movie['title'].values)

if st.button('Get recommendation'):
    movies_list, movie_img = recommend(options)
    a, b, c, d, e, f = st.columns(6)
    with a:
        st.text(movies_list[0])
        st.image(movie_img[0])
    with b:
        st.text(movies_list[1])
        st.image(movie_img[1])
    with c:
        st.text(movies_list[2])
        st.image(movie_img[2])
    with d:
        st.text(movies_list[3])
        st.image(movie_img[3])
    with e:
        st.text(movies_list[4])
        st.image(movie_img[4])
    with f:
        st.text(movies_list[5])
        st.image(movie_img[5])
st.image('watching.jpg')
