"""Streamlit interface for the Book Recommendation Engine."""

from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.neighbors import NearestNeighbors


PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "Books Dataset"


@st.cache_resource
def build_recommender() -> tuple[pd.DataFrame, NearestNeighbors, pd.DataFrame]:
    """Load the included ratings and fit the same model used in the notebook."""
    books = pd.read_csv(
        DATA_DIR / "BX-Books.csv",
        sep=";",
        encoding="latin-1",
        on_bad_lines="skip",
        low_memory=False,
    )
    ratings = pd.read_csv(
        DATA_DIR / "BX-Book-Ratings.csv",
        sep=";",
        encoding="latin-1",
        on_bad_lines="skip",
        low_memory=False,
    )
    books.columns = [
        "isbn",
        "title",
        "author",
        "year",
        "publisher",
        "image_s",
        "image_m",
        "image_l",
    ]
    ratings.columns = ["user_id", "isbn", "rating"]
    interactions = ratings.merge(
        books[["isbn", "title", "author", "image_m"]], on="isbn", how="inner"
    )
    interactions = interactions[interactions["rating"] > 0].copy()
    active_readers = interactions.groupby("user_id").size().loc[lambda values: values >= 35].index
    popular_books = interactions.groupby("title").size().loc[lambda values: values >= 25].index
    filtered = interactions[
        interactions["user_id"].isin(active_readers)
        & interactions["title"].isin(popular_books)
    ]
    pivot = filtered.pivot_table(
        index="title", columns="user_id", values="rating", fill_value=0
    )
    model = NearestNeighbors(metric="cosine", algorithm="brute", n_neighbors=6)
    model.fit(pivot.values)
    metadata = (
        interactions.sort_values("rating", ascending=False)
        .drop_duplicates("title")
        .set_index("title")
    )
    return pivot, model, metadata


def recommend(
    title: str,
    pivot: pd.DataFrame,
    model: NearestNeighbors,
    metadata: pd.DataFrame,
) -> pd.DataFrame:
    """Return the five closest books and useful display metadata."""
    position = pivot.index.get_loc(title)
    distances, indices = model.kneighbors(
        pivot.iloc[position].to_numpy().reshape(1, -1), n_neighbors=6
    )
    result = pd.DataFrame(
        {
            "title": pivot.index[indices[0][1:]],
            "similarity": 1 - distances[0][1:],
        }
    )
    result["author"] = result["title"].map(metadata["author"])
    result["cover"] = result["title"].map(metadata["image_m"])
    return result


st.set_page_config(page_title="Book Recommendation Engine", page_icon="📚", layout="wide")
st.title("Book Recommendation Engine")
st.caption("Item-based collaborative recommendations from the included Book-Crossing ratings")

pivot_matrix, recommender, book_metadata = build_recommender()
selected = st.selectbox("Select a book", pivot_matrix.index.tolist())

if st.button("Show recommendations", type="primary"):
    recommendations = recommend(selected, pivot_matrix, recommender, book_metadata)
    columns = st.columns(5)
    for column, row in zip(columns, recommendations.itertuples(index=False)):
        with column:
            if isinstance(row.cover, str) and row.cover.startswith("http"):
                st.image(row.cover, use_container_width=True)
            st.markdown(f"**{row.title}**")
            st.caption(str(row.author))
            st.metric("Similarity", f"{row.similarity:.3f}")
