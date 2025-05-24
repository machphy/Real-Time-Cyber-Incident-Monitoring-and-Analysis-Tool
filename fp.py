import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import precision_recall_curve, auc
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Step 1: Create synthetic dataset for classification
X, y = make_classification(n_samples=1000, n_features=6, n_informative=4, 
                           n_redundant=1, n_classes=2, random_state=42)

# Step 2: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Step 4: Get prediction probabilities for class 1
y_probs = clf.predict_proba(X_test)[:, 1]

# Step 5: Calculate Precision-Recall curve values
precision, recall, thresholds = precision_recall_curve(y_test, y_probs)

# Step 6: Calculate AUC (Area Under the Curve)
auc_score = auc(recall, precision)

# Step 7: Plot FP vs Detection Tradeoff
plt.figure(figsize=(8, 6))
plt.plot(precision, recall, color='b', label=f'Precision-Recall curve (AUC = {auc_score:.2f})')
plt.xlabel('False Positive Rate (1 - Precision)')
plt.ylabel('True Positive Rate (Recall)')
plt.title('FP vs Detection Rate Tradeoff')
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()

# Save the plot as image
plt.savefig("img4_fp_vs_detection_tradeoff.png", dpi=300)

# Show the plot
plt.show()
