import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
file_path = 'fifa_eda_stats.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Filter players with age above 21
df_filtered = df[df['Age'] > 21]

# Create and display the histogram
plt.figure(figsize=(10, 6))
plt.hist(df_filtered['Age'], bins=range(22, df_filtered['Age'].max() + 2), edgecolor='orange')
plt.title('Number of Players Older Than 21 Years of Age')
plt.xlabel('Age')
plt.ylabel('Number of Players')

plt.yticks(range(0, df_filtered['Age'].value_counts().max() + 10, 2))
plt.xticks(range(22, df_filtered['Age'].max() + 2))
plt.grid(axis='y', linestyle='-', alpha=0.7)
plt.show()