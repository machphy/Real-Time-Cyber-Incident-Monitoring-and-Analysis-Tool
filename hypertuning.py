import matplotlib.pyplot as plt
import pandas as pd

# Define the feature table
data = {
    "Feature": ["src_port", "dst_port", "proto_id", "entropy", "packet_size", "conn_frequency"],
    "Description": [
        "Source port from request origin",
        "Destination port (e.g., 22 for SSH)",
        "Protocol type (TCP=6, UDP=17)",
        "Shannon entropy of request",
        "Size of packet (in bytes)",
        "Requests per 10s from source IP"
    ],
    "Example": [443, 22, 6, 3.78, 1024, 15]
}

df = pd.DataFrame(data)

# Plot the table
fig, ax = plt.subplots(figsize=(10, 3))
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)

plt.title("Dataset Feature Representation", fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig("images/dataset_feature_representation.png", dpi=300)
plt.show()
