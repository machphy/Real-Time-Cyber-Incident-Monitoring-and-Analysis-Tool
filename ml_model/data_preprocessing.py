import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    try:
        data = pd.read_excel(file_path)  
        print(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    df.drop_duplicates(inplace=True)
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        df[column].fillna(df[column].mean(), inplace=True)
    for column in df.select_dtypes(include=['object']).columns:
        df[column].fillna(df[column].mode()[0], inplace=True)
    return df

def preprocess_data(df):
    if 'category_column' in df.columns:
        df = pd.get_dummies(df, columns=['category_column'], drop_first=True)
    
    from sklearn.preprocessing import StandardScaler
    numerical_columns = ['numerical_column1', 'numerical_column2']
    
    if all(col in df.columns for col in numerical_columns):
        scaler = StandardScaler()
        df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
    
    return df

def split_data(df, target_column):
    if target_column not in df.columns:
        print(f"Error: Target column '{target_column}' not found in the dataset.")
        return None, None, None, None
    
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":

    file_path = 'ml_model/data/raw/cybersecurity_attacks.xlsx'
    
    data = load_data(file_path)
    if data is not None:
        cleaned_data = clean_data(data)
        preprocessed_data = preprocess_data(cleaned_data)
        
        X_train, X_test, y_train, y_test = split_data(preprocessed_data, target_column='attack_type')

        if X_train is not None:
            print("Data preprocessing complete!")  
        else:
            print("Error during data preprocessing.")

    data = load_data('ml_model/data/raw/cybersecurity_attacks.xlsx')

    print("Data loaded successfully ok")
    print(data.head())  # Display first 5 rows of data