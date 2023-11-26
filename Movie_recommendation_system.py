import streamlit as st
import pickle
import pandas as pd
import requests
import streamlit.components.v1 as com
import os

def fetch_poster(movie_id):
    # TMDB API = cf4e4064a7e007c24605567fb4fd019c
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cf4e4064a7e007c24605567fb4fd019c&language=en-US'.format(movie_id))
    data = response.json()
    
    # Use get with a default value to handle the case where 'poster_path' is not present
    poster_path = data.get('poster_path')
    
    if poster_path is not None:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "No poster available"  # or another appropriate default value

    

# defining a movie recommendation function
def recommend (movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distance = similar_movie[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse = True, key = lambda x:x[1])[1:11]
    
    recommended_movies = []
    recommended_movie_poster = []
    
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API (Application Programming Interface)        
        recommended_movie_poster.append(fetch_poster(movie_id))
        
        
    return recommended_movies,recommended_movie_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)


similar_movie = pickle.load(open('similar_movie.pkl','rb'))

st.title('Movie Recommendation System')

selected_movie = st.selectbox(
                      'Enter one movie you want to get similar to that.',
                      movies['title'].values)

if st.button('Recommend'):
    movie_name,movie_poster = recommend(selected_movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.subheader(movie_name[0])        # to print name of the 1st movie
        st.image(movie_poster[0])
        
    with col2:
        st.subheader(movie_name[1])        # to print name of the 2nd movie
        st.image(movie_poster[1])
    
    with col3:                          # to print name of the 3rd movie 
        st.subheader(movie_name[2])
        st.image(movie_poster[2])
    
    with col4:                          # to print name of the 4th movie
        st.subheader(movie_name[3])
        st.image(movie_poster[3])
    
    with col5:                          # to print name of the 5th movie
        st.subheader(movie_name[4])
        st.image(movie_poster[4])

    # creating the columns in next line
    col6, col7, col8, col9, col10 = st.columns(5)
    
    with col6:                          # to print name of the 6th movie
        st.subheader(movie_name[5])        
        st.image(movie_poster[5])

    with col7:                          # to print name of the 7th movie
        st.subheader(movie_name[6])         
        st.image(movie_poster[6])
    
    with col8:                          # to print name of the 8th movie
        st.subheader(movie_name[7])        
        st.image(movie_poster[7])

    with col9:                          # to print name of the 9th movie
        st.subheader(movie_name[8])
        st.image(movie_poster[8])
        
    with col10:                         # to print name of the 10th movie
        st.subheader(movie_name[9])
        st.image(movie_poster[9])     