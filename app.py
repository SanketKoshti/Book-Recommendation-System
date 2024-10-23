import pickle
import streamlit as st
import numpy as np

# Assuming you have a bookRecommendation module with necessary methods
from bookRecommendation import recommend_book, fetch_p, books

st.header("Book Recommendation System")

# Load the pre-trained model and data files
model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_ratings.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))


def fetch_poster(suggestion):
    book_names = []
    ids_index = []
    poster_url = []

    # Get book names based on suggestions
    for book_id in suggestion[0]:  # Loop over the suggestions, not just suggestion[0]
        book_names.append(book_pivot.index[book_id])

    # Fetch poster URLs
    for book in book_names:  # Loop over all the suggested book names
        ids = np.where(final_rating['Title'] == book)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['img-url']
        poster_url.append(url)

    return poster_url, book_names  # Return both poster URLs and book names


def recommend_books(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]  # Find the index of the selected book
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    poster_url, book_list = fetch_poster(suggestions)

    return book_list, poster_url


# Streamlit UI for book selection
selected_book = st.selectbox("Type or Select a book", books_name)

if st.button('Show Recommendation'):
    recommended_books, poster_urls = recommend_books(selected_book)

    num_books = len(recommended_books)

    col1, col2, col3, col4, col5 = st.columns(5)

    columns = [col1, col2, col3, col4, col5]

    # Display recommended books and their posters (if available)
    for idx in range(min(num_books, 5)):  # Limit to 5 recommendations
        with columns[idx]:
            st.text(recommended_books[idx])
            st.image(poster_urls[idx])


#mkdir -p ~/.streamlit/

#echo "\
#[server]\n\
#port=$PORT\n\
#enableCORS=false\n\
#headless=true\n\
#\n\
#" > ~/.streamlit/config.toml
