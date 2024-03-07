import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    
    data = response.json()
    
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
  


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
    recommend_movies = []
    recommend_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        #fetch poster from API
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_posters
           

#dataframe 
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

#similarity
similarity = pickle.load(open('similarity.pkl', 'rb'))


#for title
st.title('Movie Recommender System')

#select box 
select_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',
    movies['title'].values)

# create Button
if st.button('Recommend'):
    #create a function for recommend
    names, posters = recommend(select_movie_name)
    
    cols = st.columns(5)
    with cols[0]:
        st.text(names[0])
        st.image(posters[0])

    with cols[1]:
        st.text(names[1])
        st.image(posters[1])

    with cols[2]:
        st.text(names[2])
        st.image(posters[2])

    with cols[3]:
        st.text(names[3])
        st.image(posters[3])

    with cols[4]:
        st.text(names[4])
        st.image(posters[4])


#background image set
import streamlit as st
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('pic.jpeg')    

import streamlit as st
import base64

#backgroung image flicker nhi hogi.
@st.cache_data
def load_background_image(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    return encoded_string

def add_bg_from_local(image_file):
    encoded_image = load_background_image(image_file)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"jpeg"};base64,{encoded_image});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local('pic.jpeg')
