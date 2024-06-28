import pandas as pd
import matplotlib.pyplot as plt

file_path = 'airbnb.csv'  
df = pd.read_csv(file_path)

df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

df_filtered = df[df['rating'] > 4]

plt.figure(figsize=(10, 6))
plt.hist(df_filtered['rating'], bins=10, edgecolor='black')
plt.title('Airbnb ratings with Rating Higher Than 4')
plt.xlabel('Rating')
plt.ylabel('Number of ratings')
plt.grid(axis='y', linestyle='-')

plt.show()