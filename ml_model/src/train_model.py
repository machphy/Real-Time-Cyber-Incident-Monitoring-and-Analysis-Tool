import pandas as pd
import json
import os

# Define directories
BASE_DIR = "/home/rajeev/Downloads/Real-Time-Cyber-Incident-Monitoring-and-Analysis-Tool/ml_model"
DATA_DIR = os.path.join(BASE_DIR, "data/raw")  # Adjusted path

# Load the Excel dataset
file_path = os.path.join(DATA_DIR, "Cyberattack Annotated Dataset 10_updated.xlsx")
df_tweets = pd.read_excel(file_path)

# Inspect the first few rows of the data to understand its structure
print("Inspecting raw data:")
print(df_tweets.head())

# Check the available columns in the dataset
print(f"Available columns: {df_tweets.columns}")

# Assuming the dataset contains 'Predicted_Label' that gives the classification (positive/negative)
if "Predicted_Label" in df_tweets.columns:
    print("✅ 'Predicted_Label' column found, proceeding with further processing.")
    
    # You can extract a simple label based on the 'Predicted_Label' column if needed
    # For example, if 'Predicted_Label' contains categories like 'CA-negative' and 'CA-positive'
    # You can assign a binary label like 0 for 'negative' and 1 for 'positive'
    df_tweets['label'] = df_tweets['Predicted_Label'].apply(
        lambda x: 1 if 'positive' in x.lower() else 0
    )

    # Now you can proceed with further processing, feature extraction, or any other analysis
    print("Labels have been assigned based on the 'Predicted_Label'.")

else:
    print("❌ 'Predicted_Label' column missing in the dataset.")

# You can also handle missing values or additional preprocessing if necessary
df_tweets.dropna(subset=['Predicted_Label'], inplace=True)

# Further analysis, feature extraction, or model training could follow here.
