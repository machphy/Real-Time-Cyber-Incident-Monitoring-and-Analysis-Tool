import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Load the data
df = pd.read_csv('../data/your_training_data.csv')  # replace with your training data path
X = df['clean_text']
y = df['label']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text data
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Train the model
model = RandomForestClassifier()
model.fit(X_train_vec, y_train)

# Save the model
with open('../models/cyberattack_model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save the vectorizer
with open('../models/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
