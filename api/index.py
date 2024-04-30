from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import sqlite3
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the GloVe model into a global variable when the script is run.
#def load_glove_model(glove_file="glove.6B.100d.txt"):
def load_glove_model(glove_file):
    print(f"Loading GloVe model from {glove_file}")
    glove_model = {}
    with open(glove_file, 'r', encoding="utf8") as f:
        for line in f:
            # Explicitly splitting by space ' ' instead of default to avoid issues with non-breaking spaces
            split_line = line.strip().split(' ')
            word = split_line[0]
            try:
                # Now, ensuring that we capture the rest of the line as the embedding, skipping malformed lines.
                embedding = np.array([float(val) for val in split_line[1:]], dtype=np.float32)
                glove_model[word] = embedding
            except ValueError:
                # Log or handle embeddings that couldn't be processed due to unexpected characters/formatting
                print(f"Skipped line due to parsing error: {line[:50]}...")
    print(f"GloVe loaded with {len(glove_model)} words.")
    return glove_model

def document_vector_glove(text):
    words = word_tokenize(text.lower())
    vectors = [glove_model.get(word, np.zeros((300,))) for word in words]
    #change x to dimensions of glove model being used, np.zeroes((X,)))
    # Debugging: Ensure all vectors are of the expected shape.
    for v in vectors:
        if v.shape != (300,):
            print(f"Unexpected vector shape: {v.shape}")
            # Add additional logging if needed

    return np.mean(vectors, axis=0) if vectors else np.zeros((300,))

# Load and process the video table database only once when the script is run.
def load_video_vectors():
    print("Starting pre-processing video_vectors")
    conn = sqlite3.connect('YTvideos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Title, Description, SubtitleBOW, Links FROM Videos")
    videos = cursor.fetchall()
    conn.close()

    video_vectors = []
    for title, description, subtitle_bow, link in videos:
        combined_text = ' '.join(filter(None, [title, description, subtitle_bow]))
        video_vector = document_vector_glove(combined_text)
        video_vectors.append((title, video_vector, link))
    print("Finished pre-processing video_vectors")
    return video_vectors

# Load the GloVe model and video vectors before starting the server
glove_model = load_glove_model("glove.840B.300d.txt")
video_vectors = load_video_vectors()

@app.route('/relevant-videos', methods=['POST'])
def get_relevant_videos():
    data = request.get_json()
    flashcard_content = data['content']
    top_k = data.get('top_k', 9)

    flashcard_vector = document_vector_glove(flashcard_content)

    similarities = []
    for title, video_vector, link in video_vectors:
        similarity = cosine_similarity([flashcard_vector], [video_vector])[0][0]
        similarities.append((title, similarity, link))

    # Sort based on similarities and select top_k
    relevant_videos = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_k]

    return jsonify([{"Title": title, "Similarity": similarity, "Link": link} for title, similarity, link in relevant_videos])

if __name__ == '__main__':
    app.run()