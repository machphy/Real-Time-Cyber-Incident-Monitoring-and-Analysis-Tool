import matplotlib.pyplot as plt
import pandas as pd

# Replace this with your actual threat labels from your dataset
# Example:
# df = pd.read_csv("data/log_dataset.csv")
# y = df["label"]

# Sample class distribution
y = pd.Series([0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 0, 1, 5, 5, 5, 5, 5, 5])  # Example data

# Mapping labels (you should use your actual labels)
label_names = {
    0: "Normal",
    1: "Malware",
    2: "Phishing",
    3: "DDoS",
    4: "Brute-force",
    5: "Suspicious"
}

label_counts = y.value_counts().sort_index()
labels = [label_names[i] for i in label_counts.index]
sizes = label_counts.values
colors = plt.get_cmap("Set3").colors[:len(labels)]

# Plotting pie chart
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, colors=colors)
plt.title("Threat Class Distribution")
plt.tight_layout()
plt.savefig("threat_class_distribution.png", dpi=300)
plt.show()
