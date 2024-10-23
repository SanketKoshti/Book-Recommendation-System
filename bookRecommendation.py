
import streamlit as st
import pandas as pd
import pickle
import requests


def fetch_p(m_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=7c1b29091b8ce2b0516521ab48c89744&language=en-USb48c89744/285".format(
        m_id)
    data = requests.get(url)
    data = data.json()
    p_path = data['poster_path']
    p_path = "http://image.tmdb.org/t/p/w500" + p_path
    return p_path


similarity = pickle.load(open('artifacts/model.pkl', 'rb'))


def recommend_book(book_name):
    index = books[books['Title'] == books].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    return distances


st.title("Book Recommendation System")

book_dict = pickle.load(open('artifacts/books_name.pkl', 'rb'))
books = pd.DataFrame(book_dict)

option = st.selectbox(
    'Books',
    books['Title'].values)

books_rec = []
if st.button('Recommend'):
    # recommend() function return list of distance between each movie
    books_rec = recommend_book(option)
    st.subheader('Top 5 :blue[books] are :sunglasses: \n\n')

col = st.columns(5)

k = 0;
for i in books_rec[:5]:
    with col[k]:
        j = k + 1
        st.text(str(j) + ": " + books.iloc[i[0]].title)
        img_path = fetch_p(books.iloc[i[0]].movie_id)
        st.write("\n")
        st.image(img_path)
        k += 1
