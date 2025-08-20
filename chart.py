import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
num_customers = 200
cac = np.random.normal(loc=50, scale=15, size=num_customers)
clv = (cac * np.random.normal(loc=4, scale=1, size=num_customers)) + np.random.normal(loc=50, scale=30, size=num_customers)
clv = np.maximum(0, clv) # Ensure CLV is not negative
marketing_channel = np.random.choice(['Social Media', 'Organic Search', 'Paid Search', 'Email'], size=num_customers, p=[0.3, 0.3, 0.2, 0.2])

data = pd.DataFrame({
    'Customer Acquisition Cost': cac,
    'Customer Lifetime Value': clv,
    'Marketing Channel': marketing_channel
})

# Set professional styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create scatterplot
plt.figure(figsize=(8, 8))
scatterplot = sns.scatterplot(
    data=data,
    x='Customer Acquisition Cost',
    y='Customer Lifetime Value',
    hue='Marketing Channel',
    palette='viridis',
    s=100,
    alpha=0.7,
    edgecolor='w',
    linewidth=0.5
)

# Style the chart
plt.title('Customer Lifetime Value vs. Acquisition Cost', fontsize=16, weight='bold')
plt.xlabel('Customer Acquisition Cost (USD)', fontsize=12)
plt.ylabel('Customer Lifetime Value (USD)', fontsize=12)
plt.legend(title='Marketing Channel', fontsize=10)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Save the chart
plt.savefig('chart.png', dpi=64, bbox_inches='tight')