import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# Ensure necessary downloads
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Define paths
DATA_DIR = "../data/"
MODEL_DIR = "../models/"
os.makedirs(MODEL_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv(os.path.join(DATA_DIR, "predefined_dataset.csv"))

# Text Cleaning Function
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r"\W", " ", text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    text = " ".join([word for word in text.split() if word not in stop_words])  # Remove stopwords
    return text

# Apply text cleaning
df["cleaned_text"] = df["Incident"].astype(str).apply(clean_text)

# Convert text into numerical format (TF-IDF)
vectorizer = TfidfVectorizer(max_features=500)
X = vectorizer.fit_transform(df["cleaned_text"]).toarray()

# Label encoding
encoder = LabelEncoder()
y = encoder.fit_transform(df["Details"])

# Save preprocessed data & models
pickle.dump(vectorizer, open(os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl"), "wb"))
pickle.dump(encoder, open(os.path.join(MODEL_DIR, "label_encoder.pkl"), "wb"))
pickle.dump(X, open(os.path.join(DATA_DIR, "X_data.pkl"), "wb"))
pickle.dump(y, open(os.path.join(DATA_DIR, "y_data.pkl"), "wb"))

print("✅ Data preprocessing completed successfully!")
