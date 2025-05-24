import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize

# 1️⃣ Generate synthetic multi-class data
X, y = make_classification(
    n_samples=500,
    n_features=6,
    n_classes=3,
    n_informative=4,
    n_redundant=1,
    random_state=42
)

# 2️⃣ Split the dataset (stratify to preserve class distribution)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)

# 3️⃣ Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 4️⃣ Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues",
            xticklabels=np.unique(y), yticklabels=np.unique(y))
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=300)
print("[✅] Confusion matrix saved as confusion_matrix.png")
plt.show()

# 5️⃣ ROC Curve (Multiclass One-vs-Rest)
y_score = model.predict_proba(X_test)
y_bin = label_binarize(y_test, classes=np.unique(y))
n_classes = y_bin.shape[1]

# Debug info
print("y_test classes:", np.unique(y_test))
print("Shape of y_score:", y_score.shape)
print("Shape of y_bin:", y_bin.shape)

fpr = dict()
tpr = dict()
roc_auc = dict()

plt.figure(figsize=(8, 6))
for i in range(n_classes):
    print(f"Plotting ROC for class {i}")
    fpr[i], tpr[i], _ = roc_curve(y_bin[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])
    plt.plot(fpr[i], tpr[i], label=f"Class {i} (AUC = {roc_auc[i]:.2f})")

plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Multiclass")
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig("roc_curve_debug.png", dpi=300)
print("[✅] ROC curve saved as roc_curve_debug.png")
plt.show()
