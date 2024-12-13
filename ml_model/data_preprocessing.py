import pandas as pd
import os
from sklearn.model_selection import train_test_split

# Paths
RAW_DATA_PATH = os.path.join(os.getcwd(), "data", "raw", "data.csv")
PROCESSED_DATA_DIR = os.path.join(os.getcwd(), "data", "processed")

def load_data(filepath):
    """Load raw data from CSV or API."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Perform basic cleaning like handling missing values and duplicates."""
    df = df.dropna()  # Remove rows with missing values
    df = df.drop_duplicates()  # Remove duplicate rows
    return df

def feature_engineering(df):
    """Create new features to enhance model performance."""
    df['new_feature'] = df['column_name'].apply(lambda x: x * 2)  # Example logic
    return df

def split_data(df):
    """Split data into training and testing sets."""
    X = df.drop('target_column', axis=1)
    y = df['target_column']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def save_data(X_train, X_test, y_train, y_test):
    """Save processed data to disk."""
    if not os.path.exists(PROCESSED_DATA_DIR):
        os.makedirs(PROCESSED_DATA_DIR)
    X_train.to_csv(os.path.join(PROCESSED_DATA_DIR, "X_train.csv"), index=False)
    X_test.to_csv(os.path.join(PROCESSED_DATA_DIR, "X_test.csv"), index=False)
    y_train.to_csv(os.path.join(PROCESSED_DATA_DIR, "y_train.csv"), index=False)
    y_test.to_csv(os.path.join(PROCESSED_DATA_DIR, "y_test.csv"), index=False)

if __name__ == "__main__":
    data = load_data(RAW_DATA_PATH)  # Load the raw data
    data = clean_data(data)  # Clean the data
    data = feature_engineering(data)  # Perform feature engineering
    X_train, X_test, y_train, y_test = split_data(data)  # Split data into train and test sets
    save_data(X_train, X_test, y_train, y_test)  # Save the processed data
    print("Data preprocessing complete. Processed files saved.")
