from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import sqlite3
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)
CORS(app)

def load_glove_model(glove_file):
    print(f"Loading GloVe model from {glove_file}")
    glove_model = {}
    with open(glove_file, 'r', encoding="utf8") as f:
        for line in f:
            split_line = line.strip().split(' ')
            word = split_line[0]
            try:
                embedding = np.array([float(val) for val in split_line[1:]], dtype=np.float32)
                glove_model[word] = embedding
            except ValueError:
                print(f"Skipped line due to parsing error: {line[:50]}...")
    print(f"GloVe loaded with {len(glove_model)} words.")
    return glove_model

def load_video_vectors(save_path='video_vectors.npy', links_save_path='video_links.npy'):
    # Check if preprocessed files exist
    if os.path.exists(save_path) and os.path.exists(links_save_path):
        print("Loading pre-processed video vectors")
        video_vectors = np.load(save_path, allow_pickle=True)
        video_links = np.load(links_save_path, allow_pickle=True)
        # Ensure zipping matches the expected structure (tuple of title, vector, link)
        return [(video_links[idx][0], video_vectors[idx], video_links[idx][1]) for idx in range(len(video_vectors))]

    print("Pre-processed video vectors not found, starting processing...")
    conn = sqlite3.connect('YTvideos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Title, Description, SubtitleBOW, Links FROM Videos")
    videos = cursor.fetchall()
    conn.close()

    video_vectors = []
    video_links = []
    for title, description, subtitle_bow, link in videos:
        combined_text = ' '.join(filter(None, [title, description, subtitle_bow]))
        video_vector = document_vector_glove(combined_text)
        video_vectors.append(video_vector)
        video_links.append((title, link))

    # After processing, save the vectors and links for future use
    np.save(save_path, video_vectors)
    np.save(links_save_path, video_links)

    # Reconstruct and return the expected structure
    return [(video_links[idx][0], video_vectors[idx], video_links[idx][1]) for idx in range(len(video_vectors))]

def document_vector_glove(text):
    words = word_tokenize(text.lower())
    vectors = [glove_model.get(word, np.zeros((300,))) for word in words]
    for v in vectors:
        if v.shape != (300,):
            print(f"Unexpected vector shape: {v.shape}")

    return np.mean(vectors, axis=0) if vectors else np.zeros((300,))

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

    relevant_videos = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_k]
    return jsonify([{"Title": title, "Similarity": similarity, "Link": link} for title, similarity, link in relevant_videos])

if __name__ == '__main__':
    app.run()