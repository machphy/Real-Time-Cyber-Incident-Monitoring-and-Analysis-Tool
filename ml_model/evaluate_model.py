import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import pickle

test_data = pd.read_csv('../data/processed/test_data.csv')
X_test = test_data.drop('target', axis=1)
y_test = test_data['target']

with open('../models/classifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy:- {accuracy}')  
print('Classification Report here:- Done')
print(report)
