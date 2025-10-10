import pandas as pd  
import seaborn as sns  
import matplotlib.pyplot as plt  
from sklearn.ensemble import RandomForestClassifier  
from sklearn.model_selection import GridSearchCV, train_test_split  
from sklearn.preprocessing import MinMaxScaler  
import os

# Step 1: Data Preparation
# Load your dataset
df = pd.read_csv("data/log_dataset.csv")  # Ensure this path is correct

# Select features and target
X = df[["src_port", "dst_port", "packet_size", "protocol"]]  # Adjust as needed
y = df["label"]

# Normalize features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 3: Hyperparameter tuning
param_grid = {
    'n_estimators': [10, 50, 100, 150],
    'max_depth': [3, 5, 10, 15],
    'min_samples_split': [2, 5, 10],
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=3,
    scoring='accuracy',
    return_train_score=True
)

# Fit model
grid_search.fit(X_train, y_train)

# Step 4: Convert results to a DataFrame
results_df = pd.DataFrame(grid_search.cv_results_)

# Optional: Convert parameters to int (sometimes they are stored as object)
results_df['param_n_estimators'] = results_df['param_n_estimators'].astype(int)
results_df['param_max_depth'] = results_df['param_max_depth'].astype(int)
results_df['param_min_samples_split'] = results_df['param_min_samples_split'].astype(int)

# Filter for a specific min_samples_split value to enable clean pivot
filtered_results = results_df[results_df['param_min_samples_split'] == 2]

# Pivot table to visualize effect of max_depth and n_estimators
pivot_table = filtered_results.pivot(
    index='param_max_depth',
    columns='param_n_estimators',
    values='mean_test_score'
)

# Step 5: Generate Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt=".3f")
plt.title("Hyperparameter Tuning Heatmap (Accuracy)")
plt.xlabel("n_estimators")
plt.ylabel("max_depth")
plt.tight_layout()

# Ensure the output directory exists
os.makedirs("images", exist_ok=True)

# Save and show heatmap
plt.savefig("images/gridsearch_heatmap.png", dpi=300)
plt.show()
