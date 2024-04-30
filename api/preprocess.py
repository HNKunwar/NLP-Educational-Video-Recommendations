import numpy as np
import pandas as pd
import sqlite3
from nltk.tokenize import word_tokenize

def load_glove_model(glove_file="glove.6B.100d.txt"):
    """Load the GloVe model from a specified file."""
    print(f"Loading GloVe model from {glove_file}")
    glove_model = {}
    with open(glove_file, 'r', encoding="utf8") as f:
        for line in f:
            split_line = line.split()
            word = split_line[0]
            embedding = np.array([float(val) for val in split_line[1:]])
            glove_model[word] = embedding
    print(f"GloVe loaded with {len(glove_model)} words.")
    return glove_model

def document_vector_glove(text, glove_model):
    words = word_tokenize(text.lower())
    vectors = [glove_model[word] for word in words if word in glove_model]
    if len(vectors) == 0:
        return np.zeros(100)  # Return a zero-vector if no words matched in GloVe model
    else:
        return np.mean(vectors, axis=0)

glove_model = load_glove_model()


def preprocess_and_save_video_vectors():
    conn = sqlite3.connect('YTvideos.db')
    all_videos_df = pd.read_sql_query("SELECT Title, Description, SubtitleBOW FROM Videos", conn)

    all_videos_df['Title'] = all_videos_df['Title'].fillna('No Title')
    all_videos_df['Description'] = all_videos_df['Description'].fillna('No description')
    all_videos_df['SubtitleBOW'] = all_videos_df['SubtitleBOW'].fillna('')

    all_videos_df['Combined_Text'] = all_videos_df['Title'] + ' ' + all_videos_df['Description'] + ' ' + all_videos_df['SubtitleBOW']

    all_videos_df['GloVe_Vector'] = all_videos_df['Combined_Text'].apply(
        lambda x: document_vector_glove(x, glove_model)
    )

    # Convert vectors to bytes for storage
    all_videos_df['GloVe_Vector'] = all_videos_df['GloVe_Vector'].apply(
        lambda x: x.astype(np.float32).tobytes()
    )

    all_videos_df[['Title', 'GloVe_Vector']].to_sql('VideoVectors', conn, if_exists='replace', index=False)

    conn.close()