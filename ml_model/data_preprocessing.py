from ml_model.data_preprocessing import load_data, clean_data, feature_engineering, split_data, save_data

# my data path 
raw_data_path = "ml_model/data/raw/Cyberattack Annotated Dataset 1_updated.xlsx"
processed_data_path = "ml_model/data/processed/processed_data.csv"
train_data_path = "ml_model/data/processed/train.csv"
test_data_path = "ml_model/data/processed/test.csv"

# Load raw data
raw_data = load_data(raw_data_path)

# Clean data
cleaned_data = clean_data(raw_data)

# Perform feature engineering
engineered_data = feature_engineering(cleaned_data)

# Save the processed data
save_data(engineered_data, processed_data_path)

# Split data into training and testing sets
train_X, test_X, train_y, test_y = split_data(engineered_data, label_column="label")

# Save training and testing data in file 
train_data = train_X.copy()
train_data["label"] = train_y
save_data(train_data, train_data_path)

test_data = test_X.copy()
test_data["label"] = test_y
save_data(test_data, test_data_path)

print("Data preparation is complete.")
