import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Step 1: Simulated IP entropy data
ip_addresses = ['192.168.1.1', '192.168.1.2', '10.0.0.5', '172.16.0.3', '192.168.1.8']
entropy_values = [2.5, 3.1, 1.8, 3.5, 2.9]

# Step 2: Plotting
plt.figure(figsize=(10, 6))

# Top - Display the formula
plt.subplot(2, 1, 1)
plt.axis('off')
plt.text(0.1, 0.5, r'Entropy Formula:  $H(X) = -\sum P(x_i) \log_2 P(x_i)$', fontsize=18, color='darkblue')

# Bottom - Entropy bar plot
plt.subplot(2, 1, 2)
sns.barplot(x=ip_addresses, y=entropy_values, palette="viridis")
plt.title("Entropy per Source IP", fontsize=14)
plt.xlabel("Source IP")
plt.ylabel("Entropy Value")
plt.tight_layout()

# Save image
plt.savefig("entropy_plot_formula.png", dpi=300)
plt.show()
