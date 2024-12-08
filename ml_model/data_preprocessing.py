import pandas as pd
import os

# Define the path to your dataset
RAW_DATA_PATH = os.path.join(os.getcwd(), "data", "raw", "data.xlsx")

def load_data(filepath):
    """Load raw data from Excel in file."""
    return pd.read_excel(filepath)

if __name__ == "__main__":
    # Load the data
    data = load_data(RAW_DATA_PATH)
    print("Data loaded successfully")
    print(data.head())  # Display first 5 rows of data
