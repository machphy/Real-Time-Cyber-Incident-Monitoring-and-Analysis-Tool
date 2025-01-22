import os
import json
import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Ensure NLTK stopwords are downloaded
nltk.download('stopwords')

# Define file paths
DATA_DIR = "../data/"
PROCESSED_DIR = "../processed_data/"
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Load stopwords
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
    """Function to clean text data"""
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(f'[{string.punctuation}]', '', text)  # Remove punctuation
    text = ' '.join([word for word in text.split() if word not in STOPWORDS])  # Remove stopwords
    return text

def preprocess_data():
    """Load, clean, and vectorize text data."""
    # Load Twitter data
    with open(os.path.join(DATA_DIR, "twitter_data.json"), "r") as file:
        twitter_data = json.load(file)
    
    # Load News data
    with open(os.path.join(DATA_DIR, "news_data.json"), "r") as file:
        news_data = json.load(file)
    
    # Convert to DataFrame
    twitter_df = pd.DataFrame(twitter_data)
    news_df = pd.DataFrame(news_data)
    
    # Combine both datasets
    twitter_df['source'] = 'Twitter'
    news_df['source'] = 'News'
    
    df = pd.concat([twitter_df[['text', 'source']], news_df[['headline', 'source']].rename(columns={'headline': 'text'})])
    df['clean_text'] = df['text'].apply(clean_text)
    
    # Vectorize text using TF-IDF
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(df['clean_text'])
    
    # Save preprocessed data
    with open(os.path.join(PROCESSED_DIR, "X_data.pkl"), "wb") as file:
        pickle.dump(X, file)
    with open(os.path.join(PROCESSED_DIR, "vectorizer.pkl"), "wb") as file:
        pickle.dump(vectorizer, file)
    
    print("Data preprocessing completed. Processed data saved.")

if __name__ == "__main__":
    preprocess_data()
