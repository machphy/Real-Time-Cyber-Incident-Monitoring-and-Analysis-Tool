import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """ Load data from a given file path """
    try:
        data = pd.read_excel(file_path)  # Assuming your data is in Excel format
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """ Clean the dataset by handling missing values and duplicates """
    # Removing duplicate rows
    df.drop_duplicates(inplace=True)
    
    # Filling missing values (assuming numeric columns are filled with the mean)
    df.fillna(df.mean(), inplace=True)
    
    return df

def preprocess_data(df):
    """ Perform any additional preprocessing like encoding and scaling """
    # Example of encoding categorical columns, you can customize based on your data
    # Assuming 'category_column' is categorical
    df = pd.get_dummies(df, columns=['category_column'], drop_first=True)
    
    # Scaling numerical features (example using StandardScaler)
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df[['numerical_column1', 'numerical_column2']] = scaler.fit_transform(df[['numerical_column1', 'numerical_column2']])
    
    return df

def split_data(df, target_column):
    """ Split data into features and target, then into training and testing sets """
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Splitting data into 80% train and 20% test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # Path to your dataset file
    file_path = 'path_to_your_file.xlsx'
    
    # Loading, cleaning, preprocessing, and splitting data
    data = load_data(file_path)
    if data is not None:
        cleaned_data = clean_data(data)
        preprocessed_data = preprocess_data(cleaned_data)
        X_train, X_test, y_train, y_test = split_data(preprocessed_data, target_column='target_column_name')
        print("Data preprocessing complete!")
