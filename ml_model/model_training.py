import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

data = pd.read_csv('../data/raw/your_dataset.csv')
X = data.drop('target', axis=1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

model_path = '../models/classifier.pkl'
with open(model_path, 'wb') as model_file:
    pickle.dump(model, model_file)

print(f'Model saved to {model_path}')     #i set model path in my file ok
