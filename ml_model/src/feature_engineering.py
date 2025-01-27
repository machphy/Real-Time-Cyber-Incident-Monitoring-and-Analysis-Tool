import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os
import json

# Define directories
BASE_DIR = "/home/rajeev/Downloads/Real-Time-Cyber-Incident-Monitoring-and-Analysis-Tool/ml_model"
DATA_DIR = os.path.join(BASE_DIR, "data/raw")
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Ensure model directory exists
os.makedirs(MODEL_DIR, exist_ok=True)

# Helper function to safely read CSV
def load_csv(file_path, text_column=None):
    try:
        df = pd.read_csv(file_path, encoding="utf-8", on_bad_lines="skip")
        print(f"✅ Loaded: {file_path} ({len(df)} rows)")
        if text_column and text_column in df.columns:
            return df[[text_column]].dropna()
        else:
            print(f"❌ Warning: Column '{text_column}' not found in {file_path}. Skipping.")
            return None
    except FileNotFoundError:
        print(f"❌ Error: File not found -> {file_path}")
        return None
    except pd.errors.ParserError:
        print(f"❌ Error: Parsing issue with {file_path}")
        return None

# Helper function to load tweets.json
def load_tweets_json(file_path):
    try:
        df = pd.read_json(file_path, lines=True)
        print(f"✅ Loaded: {file_path} ({len(df)} tweets)")
        if "text" in df.columns:
            return df[["text"]].rename(columns={"text": "clean_text"}).dropna()
        else:
            print("❌ Warning: 'text' column missing in tweets file.")
            return None
    except Exception as e:
        print(f"❌ Error loading tweets: {e}")
        return None

# Load datasets
df_twitter = load_tweets_json(os.path.join(DATA_DIR, "tweets.csv"))  # Tweets JSON
df_news = load_csv(os.path.join(DATA_DIR, "news_clean.csv"), "Description")  # Use 'Description' column for text

# Validate data
if df_twitter is None or df_news is None:
    print("❌ Exiting: One or more required datasets are missing or invalid.")
    exit()

# Combine all text data & drop NaNs
all_text = pd.concat([df_twitter["clean_text"], df_news["Description"]]).dropna()

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(all_text)

# Save vectorizer
vectorizer_path = os.path.join(MODEL_DIR, "vectorizer.pkl")
with open(vectorizer_path, "wb") as f:
    pickle.dump(vectorizer, f)

print(f"✅ Feature extraction completed. Vectorizer saved at: {vectorizer_path}")
