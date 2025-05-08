import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

# ✅ Define paths
DATA_PATH = "data/log_dataset.csv"  # ✅ Corrected path
MODEL_PATH = "ml/threat_model.pkl"
SCALER_PATH = "ml/scaler.pkl"

# ✅ Load your dataset
try:
    df = pd.read_csv(DATA_PATH)
    print(f"✅ Dataset loaded successfully from {DATA_PATH}")
except FileNotFoundError:
    print(f"❌ Dataset not found at {DATA_PATH}")
    exit(1)

# ✅ Feature selection
required_columns = ["src_port", "dst_port", "packet_size", "protocol", "label"]
if not all(col in df.columns for col in required_columns):
    print("❌ Dataset missing one or more required columns:", required_columns)
    exit(1)

X = df[["src_port", "dst_port", "packet_size", "protocol"]]
y = df["label"]

# ✅ Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ✅ Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ✅ Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("✅ Model training complete.")

# ✅ Save model and scaler
joblib.dump(model, MODEL_PATH)
joblib.dump(scaler, SCALER_PATH)
print(f"✅ Model saved to {MODEL_PATH}")
print(f"✅ Scaler saved to {SCALER_PATH}")
